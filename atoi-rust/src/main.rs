struct Solution {}

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        // return 0 immediately on empty strings
        if s.is_empty() {
            return 0;
        }

        // constants for max i32 positive and negative
        let negmax = -(<i32>::MAX as i64 + 1) as i32;
        let posmax = <i32>::MAX as i64 as i32;

        // trim leading/trailing whitespace
        let mut trimmed = s.trim();

        // check if string starts with negative/positive sign
        let mut negative = false;
        if trimmed.starts_with("-") {
            trimmed = &trimmed[1..];
            negative = true;
        } else if trimmed.starts_with("+") {
            trimmed = &trimmed[1..];
            negative = false;
        }

        // strip leading 0s
        while trimmed.starts_with("0") {
            trimmed = &trimmed[1..];
        }

        // iterate through the chars and parse out valid digits, stopping at the
        // first non-digit value found
        let mut digits = Vec::new();
        for c in trimmed.chars() {
            let code = c as u8;
            if code < 0x30 || code > 0x39  {
                break;
            } else {
                digits.push(code - 0x30);
            }
        }

        if digits.len() > <i32>::MAX.to_string().len() {
            if negative {
                return negmax;
            }
            return posmax;
        }
        if digits.is_empty() {
            return 0;
        }

        // we have some digits, need to convert to int
        let mut result :u64 = 0;

        // use pop() to go through the parsed digits starting from the last parsed
        // i.e. from lowest place to highest, multiply 10s on each iteration.
        let mut mult :u64 = 1;
        while let Some(top) = digits.pop() {
            let next_place = top as u64 * mult;
            // break out early if the next digit place would exceed i32 MAX
            if next_place > <i32>::MAX as u64 {
                if negative {return negmax} else {return posmax};
            }
            result = result.wrapping_add(next_place);
            mult *= 10;
        }

        if negative {
            if result > <i32>::MAX as u64 {
                return negmax;
            }
            return -(result as i64) as i32;
        }
        if result > <i32>::MAX as u64 {
            return posmax;
        }
        return result as i32;

    }
}

fn main() {
    let testcases = [("234", 234), ("-234", -234), ("-0000234", -234)];
    let mut case_num = 0;
    for case in testcases {
        case_num += 1;
        let answer = Solution::my_atoi(case.0.to_string());
        assert_eq!(answer, case.1);
        println!("testcase {case_num} PASSED");
    }
}
