let buttonList = []

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
  interestButton = new_element('a', {'href': "/event?k="+desc.event_id, 'id': 'interest'+count, 'class': 'button', 'type': 'button', 'name': 'button'+count})

   let new_div = new_element('div', {'class': 'event'}, [
    new_element('div', {'class': 'event-header', 'style': 'width=500px;', 'style': 'background-color=cornflowerblue;'}),
    new_element('div', {'class': 'event-details', 'style': 'width=500px', 'style': 'height=300px'}, [

      new_element('div', {'id': 'left-side'+count, 'style': 'width=50%', 'style': 'display: inline-block'}),
      new_element('div', {'id': 'right-side'+count, 'style': 'width=50%', 'style': 'display: inline-block'}),
      //new_element('a', {'href': '{{event_url}}' },[
      interestButton
      //]
    ])]);


   let container = document.querySelector("#news-feed");
   container.insertBefore(new_div, container.children[0]);
   let left = document.querySelector("#left-side"+count);
   let right = document.querySelector("#right-side"+count);

   document.querySelector('.event-header').textContent += desc.name;
   document.querySelector('.button').textContent += "I am interested"
   left.textContent += desc.address +" " + desc.people_needed + " | ";
   right.textContent += desc.type + " " + desc.date + " " + desc.time_start + " to " + desc.time_end;

   //buttonList.push(interestButton)
   interestButton.addEventListener("click", () =>
      alert("yaay, you are interested!")
    );
   //console.log(1)
}

//displays events
function show_events() {
  let count = 0;
  fetch('/retrieve' + window.location.search, {'credentials': 'include'})
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

//event listener for interest button
