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

function insert_event(desc, count){
   let new_div = new_element('div', {'class': 'event'}, [
    new_element('div', {'class': 'event-header', 'style': 'width=500px;', 'style': 'background-color=cornflowerblue;'}),
    new_element('div', {'class': 'event-details', 'style': 'width=500px', 'style': 'height=300px'}, [

      new_element('div', {'id': 'left-side'+count, 'style': 'width=50%', 'style': 'display: inline-block'}),
      new_element('div', {'id': 'right-side'+count, 'style': 'width=50%', 'style': 'display: inline-block'})
  ])]);
   let container = document.querySelector("#news-feed");
   container.insertBefore(new_div, container.children[0]);
   let left = document.querySelector("#left-side"+count);
   let right = document.querySelector("#right-side"+count);
   left.textContent += desc.type;
   right.textContent += desc.time_start;
   console.log(1)
}

function show_events() {
  let count = 0;
  fetch('/retrieve', {'credentials': 'include'})
    .then((data) => {return data.json()})
    .then((json) => {
      for (let i in json) {
        insert_event(json[i], count);
        count++;
      }
    })
  last_refresh = new Date();
}

show_events()
