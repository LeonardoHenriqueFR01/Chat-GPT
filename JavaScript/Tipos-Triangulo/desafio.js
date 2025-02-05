// Verificando tipos de um triângulo


function tiposTriangulo(l1, l2, l3) {
    if (l1 === l2 && l1 === l3 && l2 === l3) {
        console.log('E um Equilátero.')
    
    } else if (l1 === l2 != l3) {
        console.log('E um Isóseles.')
    
    } else if (l1 != l2 != l3) {
        console.log('Escaleno')
    
    }

}

tiposTriangulo(1, 3, 2)
