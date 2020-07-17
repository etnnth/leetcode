func maxUncrossedLines(A []int, B []int) int {
    /*    
    var A []int
    var B []int
    for _, a := range LA {
        if intInSlice(a, LB) {
            A = append(A,a)
        }
    }
    for _, b := range LB {
        if intInSlice(b, A) {
            B = append(B,b)
        }
    } 
    */
    n := len(B)
    /*  
    m := len(A)
    if m>n {
        B,A = A,B
        m,n = n,m
    } 
    */ 
    dp := make([]int, n+1)
    for _, a := range A {
        for j := n-1 ; j>=0 ; j-- {
            if a == B[j] {
                dp[j+1] = dp[j] + 1
            }
        }
        for j := 0 ; j<n ; j++ {
            if dp[j] > dp[j+1] {
                dp[j+1] = dp[j]
            }
        }
    }
    return dp[n]
}

func intInSlice(a int, list []int) bool {
    for _, b := range list {
        if b == a {
            return true
        }
    }
    return false
}

