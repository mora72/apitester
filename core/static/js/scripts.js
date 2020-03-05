$( document ).ready(function() {
    var baseUrl   = 'http://localhost:8000/cidadesufs/';
    var filteruf = $('#filteruf');
    $(filteruf).change(function() {
        var filteruf = $(this).val();
        window.location.href = baseUrl + '?filteruf=' + filteruf + '&filtercidade=0';
    });

    var baseUrl   = 'http://localhost:8000/cidadesufs/';
    var filtercidade = $('#filtercidade');
    $(filtercidade).change(function() {
        var filtercidade = $(this).val();
        var filteruf = $('#filteruf').val();
        window.location.href = baseUrl + '?filteruf=' + filteruf + '&filtercidade=' + filtercidade;
    });

    // Ação do botão busca cep (click)
    var Btncep = $('#btn-cep');
    var searchForm = $('#searchcep-form');
    $(Btncep).on('click', function() {
        searchForm.submit();
    });

    // Ação do botão busca ano (click)
    //    var Btnano = $('#btn-ano');
    //    var searchForm = $('#searchano-form');
    //    $(Btnano).on('click', function() {
    //        searchForm.submit();
    //    });
});
