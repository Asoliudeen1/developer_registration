// AUTO HIDE BOOSTRAP ALERT

window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUP(500, function() {
        $(this).remove();
    })
}, 3000);