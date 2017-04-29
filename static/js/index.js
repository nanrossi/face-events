function addItem() {
    var list = document.getElementsByClassName('menu-list');
    var item = document.createElement('li');
    var a = document.createElement('a');
    a.innerHTML = document.getElementById('texto').value;
    item.appendChild(a);
    list[0].appendChild(item);
}
