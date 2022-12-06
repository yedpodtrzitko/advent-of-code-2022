use regex::Regex;

pub fn p1(data: &Vec<String>) -> i32 {
    let mut overlaps = 0;
    for line in data {
        let re_match = Regex::new(r"(\d+)\-(\d+),(\d+)\-(\d+)$").unwrap();
        let mut ranges: Vec<i32> = vec![];
        if line == "" {
            continue;
        }

        for duties in re_match.captures(line).unwrap().iter().skip(1) {
            match duties {
                Some(m) => ranges.push(m.as_str().parse::<i32>().unwrap()),
                None => println!("none {:?}", duties),
            }
        }

        //if d1_from <= d2_from and d1_to >= d2_to:
        //elif d1_from >= d2_from and d1_to <= d2_to:  # d1 is subset
        if ranges[0] <= ranges[2] && ranges[1] >= ranges[3] {
            overlaps += 1
        } else if ranges[0] >= ranges[2] && ranges[1] <= ranges[3] {
            overlaps += 1
        }
    }

    overlaps
}

pub fn p2(data: &Vec<String>) -> i32 {
    let mut overlaps = 0;
    for line in data {
        let re_match = Regex::new(r"(\d+)\-(\d+),(\d+)\-(\d+)$").unwrap();
        let mut ranges: Vec<i32> = vec![];
        if line == "" {
            continue;
        }

        let re_match = Regex::new(r"(\d+)\-(\d+),(\d+)\-(\d+)$").unwrap();
        for duties in re_match.captures(line).unwrap().iter().skip(1) {
            match duties {
                Some(m) => ranges.push(m.as_str().parse::<i32>().unwrap()),
                None => println!("none {:?}", duties),
            }
        }

        //if d1_from <= d2_from and d1_to >= d2_from:
        //elif d1_from >= d2_from and d1_from <= d2_to:
        if ranges[0] <= ranges[2] && ranges[1] >= ranges[2] {
            overlaps += 1
        } else if ranges[0] >= ranges[2] && ranges[0] <= ranges[3] {
            overlaps += 1
        }
    }

    overlaps
}

pub fn run(lines: &Vec<String>) {
    println!("part 1 {}", p1(lines));
    println!("part 2 {}", p2(lines));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_d3_p1() {
        let test_data: Vec<String> = vec![
            "2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8",
        ]
        .iter()
        .map(|x| x.to_string())
        .collect();

        let res = p1(&test_data);
        assert_eq!(res, 2);
    }

    #[test]
    fn test_d3_p2() {
        let test_data: Vec<String> = vec![
            "2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8",
        ]
        .iter()
        .map(|x| x.to_string())
        .collect();

        let res = p2(&test_data);
        assert_eq!(res, 4);
    }
}
