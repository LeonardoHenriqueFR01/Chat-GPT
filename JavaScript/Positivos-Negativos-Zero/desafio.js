// Crie uma função chamada verificarNumero que recebe um número como argumento e verifica se ele é positivo, negativo ou zero. A função deve imprimir uma mensagem correspondente.

function verificarNumero(num) {

    if (num === 0) {
        console.log(`O número ${num} e Zero.`)
   
    } else if (num < 0) {
        console.log(`O número ${num} é um número negativo.`)
    
    } else if (num > 0) {
        console.log(`O número ${num} é um número positivo.`)    
    
    }

}

verificarNumero(10)
