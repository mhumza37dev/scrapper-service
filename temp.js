var headers = {
  accept: "application/json, text/plain, */*",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
  "cache-control": "no-cache",
  "content-length": 187,
  "content-type": "application/json",
  "medium:": "IFRAME",
  origin: "https://bop-web.peekaboo.guru",
  ownerkey: "d98a49c8932b09184e9d5bef841d99e0",
  pragma: "no-cache",
  referer: "https://bop-web.peekaboo.guru/",
  "sec-ch-ua": `Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108`,
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "Windows",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-site",
  "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
  version: "1.0.0",
  Cookie:
    "fbp=fb.1.1672841818101.313195498; _gcl_au=1.1.568667475.1672841819; _ga=GA1.2.1207278388.1672841819; __gads=ID=be30c0a23313e962-221c1ac70fd800c0:T=1672841819:RT=1672841819:S=ALNI_MYWxpSROF9-264pZVdSSscM4yq3Pw; __gpi=UID=00000bbaaa291d0f:T=1672841819:RT=1672841819:S=ALNI_MaT1Huw7ygkKi-KrKcTNjn0R7-SmQ; _ga=GA1.3.1115765304.1673523981; _gid=GA1.3.1116659515.1673523981; _gat=1",
};

const Http = new XMLHttpRequest();

fetch("https://secure-sdk.peekaboo.guru/uljin2s3nitoi89njkhklgkj5", {
  method: "POST",
  headers: headers,
  body: {
    fksyd: "Lahore",
    n4ja3s: "Pakistan",
    js6nwf: "0",
    pan3ba: "0",
    mstoaw: "en",
    angaks: "all",
    j87asn: "_all",
    makthya: "trending",
    mnakls: 12,
    opmsta: "0",
    kaiwnua: "_all",
    klaosw: false,
  },
}).then((res) => {
  console.log(res);
});
