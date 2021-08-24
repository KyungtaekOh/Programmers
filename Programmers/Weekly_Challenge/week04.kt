class Solution {
    fun solution(table: Array<String>, languages: Array<String>, preference: IntArray): String {
        var answer: String = ""
        var lines = mutableMapOf<String, Any>()
        for (line in table){
            var temp = line.split(' ')
            var tempmap = mutableMapOf<String, Int>()
            for (idx in 1..temp.size-1){ tempmap.put(temp[idx], 5-idx+1) }
            lines.put(temp[0], tempmap)
        }

        var result = 0
        for (part in lines.entries){
            var score: MutableMap<String, Int> = part.value as MutableMap<String, Int>
            var temp = 0
            for (idx in 0..languages.size-1){
                var lang_score = score.get(languages[idx])
                if (lang_score != null){
                    temp += lang_score*preference[idx]
                }
            }
            if (result < temp){
                result = temp
                answer = part.key
            }else if (result == temp && answer.compareTo(part.key)>0){
                answer = part.key
            }
        }
        return answer
    }
}

/*
*table       ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
*languages   ["PYTHON", "C++", "SQL"]
*preference  [7, 5, 5]
*result      "HARDWARE"
*/