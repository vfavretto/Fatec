let valorFinal;
let ValorCombo;
let ValorAdd;
let valorEntrega = 0


function CalcularFinal (){
    CalcularAdd();
    CalcularEntrega();
    CalcularCombo();
    valorFinal = ValorAdd + ValorCombo + valorEntrega
    console.log(valorFinal)
    console.log(ValorAdd)
    console.log(ValorCombo)
    console.log(valorEntrega)
    document.getElementById('floatingInputDisabled').value = `${valorFinal}`
    document.getElementById('floatingTextareaDisabled').innerHTML = `Seu combo custará ${ValorCombo} com ${ValorAdd} de adicionais e ${valorEntrega} de taxa de entrega`
}

function CalcularAdd (){
    ValorAdd = 0;
    let tamanho = document.querySelectorAll("input[name='add']").length;
    let adicionais = document.querySelectorAll("input[name='add']");
    for(var i = 0 ; i < tamanho; i= i+1) {
        if (adicionais[i].checked){
            ValorAdd += Number(adicionais[i].value);
        }
    }
}
function CalcularEntrega (){
    let entrega = document.querySelectorAll("input[name='flexRadioDefault']");
    for (let i = 0; i < entrega.length; i++)
        if (entrega[i].checked) {
            valorEntrega = Number(entrega[i].value);
            break
        }
    
}

function CalcularCombo (){
    ValorCombo = Number(document.getElementById('Combos').value)
   
    
}