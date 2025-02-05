// Verifica se o número e PAR ou IMPAR

function Verificarnumero(num) {
    if (num % 2 === 0) {
        console.log(`O número ${num} é PAR.`)

    } else if (num % 2 === 1) {
        console.log(`O número ${num} é IMPAR.`)
    }
}

Verificarnumero(0)
