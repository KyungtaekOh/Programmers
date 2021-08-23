class Solution {
    fun solution(new_id: String): String {
        var answer: String = new_id.toLowerCase()
                .filter{Character.isLetterOrDigit(it) || it=='-' || it=='_' || it=='.'}
                .replace("[.]{2,}".toRegex(), ".")
                .let { if (it.first()=='.' && it.length>1) it.substring(1, it.length) else it  }
                .let { if (it.last()=='.') it.substring(0, it.length-1) else it }
                .let { if (it.length==0) "a" else it }
                .let { if (it.length>=16) it.substring(0, 15) else it }
                .let { if (it.last()=='.') it.substring(0, it.length-1) else it }
        while (answer.length<3){ answer = answer.plus(answer.last()) }
        return answer
    }
}

/*
Test case
no	new_id	                        result
예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
예2	"z-+.^."	                    "z--"
예3	"=.="	                        "aaa"
예4	"123_.def"	                    "123_.def"
예5	"abcdefghijklmn.p"	            "abcdefghijklmn"
*/