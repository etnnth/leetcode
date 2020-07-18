func findCircleNum(M [][]int) int {
    var p map[int]int
    var r map[int]int
    p = make(map[int]int)
    r = make(map[int]int)
    n := len(M)
    for i := 0 ; i < n ; i++ {
        p[i] = i
        r[i] = 0
    } 
    
    for i := 0 ; i < n ; i++ {
        for j := i ; j < n ; j++ { 
            if M[i][j] == 1 {
                union(i,j,p,r)
            }
        }
    }
    var s int
    var k []int
    for i := 0 ; i < n ; i++ {
        j := true
        f := find(i, p)
        for _,x := range k {
            if x == f {
                j = false
            }
        }
        if j {
            k = append(k, f)
            s++
        }
    }
    return s
}

func find(x int, p map[int]int) int {
    for x != p[x] {
        x = p[x]
    }
    return x
}

func union(x int, y int, p map[int]int, r map[int]int) {
    i,j := find(x,p), find(y,p)
    if i != j {
        if r[i] < r[j] {
            p[i] = j
        } else {
            p[j] = i
            if r[i] == r[j] {
                r[i]++
            }
        }
    }
}
