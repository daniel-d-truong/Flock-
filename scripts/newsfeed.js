function new_element(tag_name, attributes, children=[]){
  el = document.createElement(tag_name)
  for (let attr in attributes){
    el.setAttribute(attr, attributes[attr]);
  }
  for (let child in children){
    el.appendChild(children[child]);
  }
  return el
}

function insert_events(desc){
  let new_div = new_element('div', {'class': 'event'}, [
    new_element('div', {'src': 'meme_templates/' + desc['image_file']}),
    new_element('h2', {'class': 'line1'}, [document.createTextNode(desc['top_text'])]),
    new_element('h2', {'class': 'line2'}, [document.createTextNode(desc['bottom_text'])]),
  ]);
  let container = document.querySelector("#displayevents");
  container.insertAfter(new_div, container.children[len(container.children -1)]);
}
