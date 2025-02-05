// Crie uma função chamada verificarIdade que recebe um número representando a idade de uma pessoa e verifica se ela é menor de idade, maior de idade ou idosa.


function verificarIdade(idade) {
    if (idade < 18) {
        console.log(`Quem tem ${idade} anos de idade é menor de idade.`)
    
    } else if (idade >= 18 && idade <= 59) {
        console.log(`Quem tem ${idade} anos de idade é maior de idade.`)
    
    } else if (idade >= 60 && idade < 100) {
        console.log(`Quem tem ${idade} anos de idade é idoso.`)
    
    } else if (idade >= 100) {
        console.log(`Quem tem ${idade} anos de idade é um DEUS.`)
    
    }
}

verificarIdade(10)
verificarIdade(20)
verificarIdade(70)
verificarIdade(102)
