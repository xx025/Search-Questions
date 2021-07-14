function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) {
            return pair[1];
        }
    }
    return (false);
}

let jump = true
let kdt = setInterval(function () {

    if (document.querySelector(".add-db").textContent == "完成" ) {
        let locdata2 = window.localStorage.getItem("urlcssss");
        let data2 = JSON.parse(locdata2);
        if (data2.indexOf(location.href) == -1) {
            data2[data2.length] = location.href
            let d = JSON.stringify(data2);
            let storage = window.localStorage;
            storage.setItem("urlcssss", d);
        }

    }
    let locdata3 = window.localStorage.getItem("urlcssss");
    let data3 = JSON.parse(locdata3);
    let locdata = window.localStorage.getItem("urls");
    let data1 = JSON.parse(locdata);
    for (const datum of data1) {
        if (jump){
            for (let i = 0; i < data3.length; i++) {
            if (data3.indexOf(datum) == -1) {
                location.href = datum;
                break
            }
        }
        }

    }
}, 1000)










