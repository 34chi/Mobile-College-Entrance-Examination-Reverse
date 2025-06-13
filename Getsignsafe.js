const CryptoJS = require("crypto-js");

function w(t) {
    var {SIGN: t, str: n} = t
      , n = (n = decodeURI(n),
      CryptoJS.HmacSHA1(CryptoJS.enc.Utf8.parse(n), t));
    t = CryptoJS.enc.Base64.stringify(n).toString();
    return s(t)
}

function s(t) {
    return CryptoJS.MD5(t).toString();
}


l = w({
    SIGN: "D23ABC@#56",
    str: 'api.zjzw.cn/web/api/?keyword=&page=5&province_id=&ranktype=&request_type=1&size=20&top_school_id=[57,3238,1569,3269]&type=&uri=apidata/api/gkv3/school/lists'
})

