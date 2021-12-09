
const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('id_amount')
const resultsBox = document.getElementById('results-box')
const elementBtn = document.getElementById('submits')

console.log(elementBtn)
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value


const sendSearchData = (amount) => {
    $.ajax({
        type: 'POST',
        url : '/btc-converter/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'amount': amount,
        },
        success: (res) => {
            console.log(res)
            const data = res.data
            if (Array.isArray(data)) {
                resultsBox.innerHTML = ""
                data.forEach(amount => {
                    resultsBox.innerHTML += `
                       
                    `
                })
                
            }else{
                if (searchInput.value.length > 0){
                    resultsBox.innerHTML = `
                    <div class="form-label-group">
                            <label class="form-label" for="buysell-amount">Amount in Crypto</label>
                        </div>
                        <div class="form-control-group" >
                            <input type="text" class="form-control form-control-lg form-control-number" id="buysell-amount" name="bs-amount" readonly placeholder="${data}">
                            <div class="form-dropdown">
                                <div class="text">BTC<span>/</span></div>
                            </div>
                        </div>
                        <div class="form-note-group">
                            <span class="buysell-min form-note-alt"></span>
                            <span class="buysell-rate form-note-alt">1 USD = 0.000016 BTC</span>
                        </div>
                    `
                }else{
                    resultsBox.classList.add('not-visible')
                }
            }
        }, 

        error: (err) => {
            console.log('err')
        }

    })
}


searchInput.addEventListener('keyup', e=>{

    if (resultsBox.classList.contains('not-visible')){
        resultsBox.classList.remove('not-visible')
    }
    console.log(e.target.value)
    sendSearchData(e.target.value)

})





$(function () {
    $('#submits').attr('disabled', true);
    $('#id_amount').change(function () {
        if ($('#id_amount').val() != '' ) {
            $('#submits').attr('disabled', false);
        } else {
            $('#submits').attr('disabled', true);
        }
    });
 });


 element.addEventListener('click', e=>{

    console.log('michael woring')
 })