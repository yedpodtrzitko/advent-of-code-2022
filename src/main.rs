use std::{fs, path::Path};

mod day1;
mod day2;
mod day3;
mod day4;
mod day6;
mod day9;

fn get_data(day: i32) -> Vec<String> {
    let path_str = format!("./input/day{}", day).to_string();
    let path_obj = Path::new(&path_str);
    let raw_data = fs::read_to_string(path_obj).unwrap();
    let res: Vec<&str> = raw_data.split("\n").collect();
    res.into_iter().map(|x| x.to_string()).collect()
}

fn main() {
    let day: i32 = std::env::args().nth(1).unwrap().parse().unwrap();

    match day {
        1 => day1::run(&get_data(day)),
        2 => day2::run(&get_data(day)),
        3 => day3::run(&get_data(day)),
        4 => day4::run(&get_data(day)),
        6 => day6::run(&get_data(day)),
        9 => day9::run(&get_data(day)),
        _ => println!("day {} not implemented yet", day),
    }
}
