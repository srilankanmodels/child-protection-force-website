const login=document.querySelector('#login');
const editor=document.querySelector('#editor');
const status=document.querySelector('#status');
const page=document.querySelector('#page');
const fields=document.querySelector('#fields');
const view=document.querySelector('#view');
let originals=[];
let loadedPage='index';
async function request(path, body){
 const response=await fetch(path,body===undefined?{}:{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
 const data=await response.json();
 if(!response.ok) throw new Error(data.error);
 return data;
}
function changed(){
 return Object.fromEntries(originals.filter(field=>editor.elements.namedItem(field.id).value!==field.value).map(field=>[field.id,editor.elements.namedItem(field.id).value]));
}
async function load(){
 originals=await request('/api/content?page='+page.value);
 loadedPage=page.value;
 fields.replaceChildren();
 for(const [group,title] of [[loadedPage,'Page content'],['header','Shared header'],['footer','Shared footer']]){
  const section=document.createElement('details');
  section.open=group===loadedPage;
  const summary=document.createElement('summary');
  summary.textContent=title;
  section.append(summary);
  for(const field of originals.filter(field=>field.id.split(':')[0]===group)){
   const label=document.createElement('label');
   label.textContent={text:'Text',href:'Link destination',src:'Image URL or filename',alt:'Image description'}[field.kind];
   const input=document.createElement(field.kind==='text'&&field.value.length>70?'textarea':'input');
   input.name=field.id;
   input.value=field.value;
   input.maxLength=4000;
   label.append(input);
   section.append(label);
  }
  fields.append(section);
 }
 view.href=loadedPage==='index'?'/':'/'+loadedPage+'.html';
 login.hidden=true;
 editor.hidden=false;
}
login.addEventListener('submit',async event=>{
 event.preventDefault();
 try{
  await request('/api/login',{password:login.elements.password.value});
  login.reset();
  await load();
  status.textContent='Signed in.';
 }catch(error){status.textContent=error.message;}
});
page.addEventListener('change',async ()=>{
 if(Object.keys(changed()).length){page.value=loadedPage;status.textContent='Save your edits before switching pages.';return;}
 try{await load();status.textContent='';}catch(error){page.value=loadedPage;status.textContent=error.message;}
});
editor.addEventListener('submit',async event=>{
 event.preventDefault();
 const changes=changed();
 try{
  await request('/api/content',{page:loadedPage,changes});
  originals.forEach(field=>{if(Object.hasOwn(changes,field.id))field.value=changes[field.id];});
  status.textContent='Changes saved to the preview.';
 }catch(error){status.textContent=error.message;}
});
load().catch(error=>{if(error.message!=='Sign in first')status.textContent=error.message;});
