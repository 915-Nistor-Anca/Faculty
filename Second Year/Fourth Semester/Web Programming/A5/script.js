function filterList() {
    var input = document.getElementById("input-field").value.toUpperCase();
    var select = document.getElementById("select-field");
    for (var i = 0; i < select.length; i++) {
        var option = select.options[i];
        if (option.value.toUpperCase().indexOf(input) > -1) {
            option.style.display = "";
        } else {
            option.style.display = "none";
        }
    }
}

document.getElementById("select-field").addEventListener("change", function() {
    document.getElementById("input-field").value = this.value;
});
