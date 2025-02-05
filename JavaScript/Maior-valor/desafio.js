// Crie uma função chamada maiorNumero que recebe três números como parâmetros e retorna o maior entre eles.

function maiorNumero(n1, n2, n3) {
    if (n1 >= n2 && n1 >= n3) {
        console.log(`O número maior é o ${n1}`)
    
    } else if (n2 >= n1 && n2 >= n3) {
        console.log(`O número maior é o ${n2}`)
    
    } else {
        console.log(`O número maior é o ${n3}`)
    
    }
}

maiorNumero(1, 2, 3) 
