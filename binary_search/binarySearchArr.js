function binarySearch(arr, start, end, target) {
  if (start > end) {
    return -1 // still dont understad this base case
  }

  // let start = 0 
  // let end = arr.length - 1
  let midpoint =  Math.floor((start+end)/2)

  if (arr[midpoint] === target) {
    return midpoint
  }

  if (target < arr[midpoint]) {
    return binarySearch(arr, start, midpoint-1 ,target ) 
  }

  return binarySearch(arr, midpoint+1, end, target)
}

// function binaryUI(arr) {
//   let end = arr.length - 1 
//   binarySearch(arr, start=0, end, 10)
// }



const arr = [-1, 0, 1, 2, 3, 4, 7, 9, 10, 20]
console.log(binarySearch(arr, 0, 9, 10))
// binaryUI(arr)
