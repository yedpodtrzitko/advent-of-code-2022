use std::cmp;

fn p1(lines: &Vec<String>) -> i32 {
    let mut all_invs: Vec<Vec<i32>> = vec![];
    let mut inv: Vec<i32> = vec![];

    for line in lines {
        if line == "" {
            all_invs.push(inv);
            inv = vec![];
        } else {
            inv.push(line.parse().unwrap());
        }
    }

    let mut max_sum = 0;
    for carry in all_invs {
        max_sum = cmp::max(carry.iter().sum(), max_sum);
    }

    max_sum
}

pub fn run(lines: &Vec<String>) {
    println!("part 1 {}", p1(lines));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_d1_p1() {
        let test_data: Vec<String> = vec![
            "1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "",
            "10000",
        ]
        .iter()
        .map(|x| x.to_string())
        .collect();

        let res = p1(&test_data);
        assert_eq!(res, 24000);
    }
}
