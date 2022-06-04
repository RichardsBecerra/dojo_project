let mio_select = document.getElementById('mio');
let cat_select = document.getElementById('mov_cid');
let itm_select = document.getElementById('mov_iid');
    
mio_select.onchange = function() {
    let mio = mio_select.value;
    fetch ('/cat/' + mio).then(function(response) {
        response.json().then(function(data) {
            let i = 0;
            cat_select.innerHTML = '';
            for (cat of data.cats) {
                cat_select.options[i] = new Option (cat.cname, cat.cid);
                i++
            }
            cat_select.onchange();
        });
    });
}

cat_select.onchange = function() {
    let mio = mio_select.value;
    let cat = cat_select.value;
    fetch ('/item/' + mio + '/' + cat).then(function(response) {
        response.json().then(function(data) {
            let options = '';
            for (item of data.items) {
                options += '<option value="' + item.iid + '">' + item.iname + '</option>';
            }
            itm_select.innerHTML = options;
        });
    });
}