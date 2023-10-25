let valorPacote = 0;
let valorAdicionais;

function CalcularTotalViagem()
{
    valorAdicionais = 0;
    CalcularPacote();
    calcularAdicionais();
    document.getElementById('resultado').innerHTML = `${valorAdicionais}`
}

function calcularAdicionais(){

    let tamanho = document.querySelectorAll("input[name='adicionais']").length;
    console.log(tamanho)
    let adicionais = document.querySelectorAll("input[name='adicionais']:checked");
    console.log(adicionais)
    for(var i = 0 ; i < tamanho; i= i+1) {
        if (adicionais[i]){
            valorAdicionais += Number(adicionais[i].value);
        }
    }
    console.log (valorAdicionais);
}

function CalcularPacote(){
    let tamanho = document.querySelectorAll("input[name='pacotes']").length;
    console.log(tamanho)
    let pacotes = document.querySelectorAll("input[name='pacotes']");
     console.log(pacotes)


//    let pacotes = document.querySelector("input[name='Pacote']:checked").value

     for(var i = 0 ; i < tamanho; i++) {
        if (pacotes[i].checked) {
            console.log(pacotes[i].value);
            valorAdicionais += Number(pacotes[i].value);
            break;
        } 
     }
 }

 