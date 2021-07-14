/*

题库爬虫：
需要设置localsession

urls: [] // 要爬取的链接
urlcssss：[] //完成的连接
 */

$(".pull-right").html(" <a href=\"###\" class=\"form-btn form-btn-blue from-save\">交卷</a>\n" +
    "<a href=\"###\" class=\"form-btn form-btn-blue add-db\">add-db</a>")

$(".add-db").click(function () {

    let data = "";
    if ($('#json').val() == "") {
        console.log("null")
    } else {
        data = JSON.stringify({'questext': JSON.parse($('#json').val())})
    }
    $.ajax({
        url: "http://127.0.0.1/add_ques",
        type: "post",
        crossDomain: true,
        data: data,
        contentType: 'application/json; charset=UTF-8',
        success: function (res) {
            console.log(res)
            $(".add-db").text("完成")
            if (document.querySelector(".add-db").textContent == "完成") {
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
                if (data3.indexOf(datum) == -1) {
                    location.href = datum;
                    break
                }
            }
        },
        error: function (res) {
            console.log(res);
            console.log(1)
        }
    });
});


$(".add-db").click()