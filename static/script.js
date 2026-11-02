function copyPassword() {
    let password = document.getElementById("password").innerText;

    navigator.clipboard.writeText(password).then(function () {
        document.getElementById("copyMessage").innerText =
            "Password copied!";
    }).catch(function () {
        document.getElementById("copyMessage").innerText =
            "Copy failed!";
    });

    setTimeout(function () {
        document.getElementById("copyMessage").innerText = "";
    }, 3000);
}
