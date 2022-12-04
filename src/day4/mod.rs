fn get_item_priority(item: char) -> i32 {
    let ascii_code = item as i32;
    match ascii_code {
        65..=90 => ascii_code - 64 + 26,
        _ => ascii_code - 96,
    }
}

pub fn p1(data: &Vec<String>) -> i32 {
    let mut priority_sum = 0;
    for rucksack in data {
        let diameter = rucksack.len() / 2;
        let (c1, c2) = rucksack.split_at(diameter);
        for c in c1.chars() {
            if c2.contains(c) {
                priority_sum += get_item_priority(c);
                break;
            }
        }
    }

    priority_sum
}

pub fn run(lines: &Vec<String>) {
    println!("part 1 {}", p1(lines));
    println!("part 2 {}", p2(lines));
}

pub fn p2(data: &Vec<String>) -> i32 {
    let mut priority_sum = 0;

    let data_len = data.len();
    let mut offset = 0;
    while (offset + 3) <= data_len {
        let r1 = &data[offset];
        let r2 = &data[offset + 1];
        let r3 = &data[offset + 2];

        for c in r1.chars() {
            if r2.contains(c) && r3.contains(c) {
                priority_sum += get_item_priority(c);
                break;
            }
        }

        offset += 3;
    }

    priority_sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_d3_p1() {
        let test_data: Vec<String> = vec![
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
        .iter()
        .map(|x| x.to_string())
        .collect();

        let res = p1(&test_data);
        assert_eq!(res, 157);
    }

    #[test]
    fn test_d3_p2() {
        let test_data: Vec<String> = vec![
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
        .iter()
        .map(|x| x.to_string())
        .collect();

        let res = p2(&test_data);
        assert_eq!(res, 70);
    }
}
