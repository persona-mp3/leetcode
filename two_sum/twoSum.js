function twoSum(array, target) {
    let map = {}
    let solution = []

    // store array items in key value pairs
    array.forEach((item, index) => {
        map[item] = index
    })
    console.log('--->maps', map)
    // iterate through aray to find the desired number
    
    for (let i=0; i < array.length; i++) {
        let desiredPair = target - array[i]


        if (map[desiredPair] !== undefined && map[desiredPair] !== i) {

            console.log('two sum found', i, desiredPair, map[desiredPair])
            solution.push(i)
            solution.push(map[desiredPair])
            return solution
        }
        
        // console.log(solution)
    }

}


const answer = twoSum([2, 7, 11, 15], 9)
console.log(answer)