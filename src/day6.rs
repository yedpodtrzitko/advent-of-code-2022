use std::collections::HashSet;

use regex::Regex;

pub fn p1(data: String) -> i32 {
    let slice_length = 4;
    let mut idx = 0;
    let length = data.len();
    for idx in 0..length {
        let sliced = data[idx..idx + slice_length].chars().clone();
        let items: HashSet<char> = HashSet::from_iter(sliced.into_iter());
        if items.len() == slice_length {
            return (idx + slice_length) as i32;
        }
    }
    idx
}

pub fn p2(data: String) -> i32 {
    let slice_length = 14;
    let mut idx = 0;
    let length = data.len();
    for idx in 0..length {
        let sliced = data[idx..idx + slice_length].chars().clone();
        let items: HashSet<char> = HashSet::from_iter(sliced.into_iter());
        if items.len() == slice_length {
            return (idx + slice_length) as i32;
        }
    }
    idx
}

pub fn run(lines: &Vec<String>) {
    println!("part 1 {}", p1(lines[0].clone()));
    println!("part 2 {}", p2(lines[0].clone()));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_d6_p1() {
        let test_data: Vec<String> = vec!["mjqjpqmgbljsphdztnvjfqwrcgsmlb"]
            .iter()
            .map(|x| x.to_string())
            .collect();

        let expected_data = vec![7];

        for (idx, item) in test_data.iter().enumerate() {
            let res = p1(item.clone());
            assert_eq!(res, expected_data[idx]);
        }
    }
}
