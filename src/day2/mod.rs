pub fn p1(lines: &Vec<String>) -> i32 {
    fn get_score(line: &str) -> i32 {
        match line {
            "A X" => 4,
            "A Y" => 8,
            "A Z" => 3,
            "B X" => 1,
            "B Y" => 5,
            "B Z" => 9,
            "C X" => 7,
            "C Y" => 2,
            "C Z" => 6,
            _ => 0,
        }
    }

    let mut score = 0;
    for line in lines {
        score += get_score(line);
    }
    score
}

pub fn p2(lines: &Vec<String>) -> i32 {
    fn get_score(line: &str) -> i32 {
        match line {
            "A X" => 3,
            "A Y" => 4,
            "A Z" => 8,
            "B X" => 1,
            "B Y" => 5,
            "B Z" => 9,
            "C X" => 2,
            "C Y" => 6,
            "C Z" => 7,
            _ => 0,
        }
    }

    let mut score = 0;
    for line in lines {
        score += get_score(line);
    }

    score
}

pub fn run(lines: &Vec<String>) {
    println!("part 1 {}", p1(lines));
    println!("part 2 {}", p2(lines));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_d2_p1() {
        let test_data: Vec<String> = vec!["A Y", "B X", "C Z"]
            .iter()
            .map(|x| x.to_string())
            .collect();

        let res = p1(&test_data);
        assert_eq!(res, 15);
    }

    #[test]
    fn test_d2_p2() {
        let test_data: Vec<String> = vec!["A Y", "B X", "C Z"]
            .iter()
            .map(|x| x.to_string())
            .collect();

        let res = p2(&test_data);
        assert_eq!(res, 12);
    }
}
