// Verifica se o número e multiplo de 3, 5 ou nem um deles


function Verificarmultiplo(num) {
    if (num % 3 === 0 && num % 5 === 0) {
        console.log(`O número ${num} e multiplo de 3 é de 5.`)

    } else if (num % 5 === 0) {
        console.log(`O número ${num} é multiplo de 5.`)
    
    } else if (num % 3 === 0) {
        console.log(`O número ${num} e multiplo de 3.`)

    } else {
        console.log(`O número ${num} não é multiplo de 3 nem de 5.`)
 
    }

}

Verificarmultiplo(10)
