use std::collections::{HashMap, HashSet};

pub fn get_move_offset(d: &str) -> [i32; 2] {
    match d {
        "R" => [1, 0],
        "L" => [-1, 0],
        "U" => [0, 1],
        "D" => [0, -1],
        _ => panic!("wrong direction"),
    }
}

pub fn p1(data: &Vec<String>) -> i32 {
    let mut all_nodes: HashMap<i32, [i32; 2]> = HashMap::from([(0, [0, 0]), (1, [0, 0])]);
    let mut all_tail_pos: HashSet<[i32; 2]> = HashSet::new();

    for line in data {
        let (direction, repeat_str) = line.split_at(1);
        let repeat_int = repeat_str.trim().parse::<i32>();
        for _ in 0..=(repeat_int.unwrap() - 1) {
            for node_idx in 0..=(all_nodes.len() - 1) {
                let idx = node_idx as i32;
                let mut node_coords = *all_nodes.get(&idx).unwrap();

                if idx == 0 {
                    let mut new_pos = get_move_offset(direction);
                    new_pos[0] += node_coords[0].clone();
                    new_pos[1] += node_coords[1].clone();

                    all_nodes.insert(idx, new_pos);
                } else {
                    let diff_x = all_nodes[&(idx - 1)][0] - node_coords[0];
                    let diff_y = all_nodes[&(idx - 1)][1] - node_coords[1];
                    if (diff_x.abs() + diff_y.abs()) > 2 {
                        node_coords[0] += if diff_x > 0 { 1 } else { -1 };
                        node_coords[1] += if diff_y > 0 { 1 } else { -1 };
                    } else if diff_x.abs() > 1 {
                        node_coords[0] += if diff_x > 0 { 1 } else { -1 };
                    } else if diff_y.abs() > 1 {
                        node_coords[1] += if diff_y > 0 { 1 } else { -1 };
                    }

                    all_nodes.insert(idx, node_coords);

                    all_tail_pos.insert(node_coords.clone());
                }
            }
        }
    }
    all_tail_pos.len() as i32
}

pub fn p2(data: &Vec<String>) -> i32 {
    let mut all_nodes: HashMap<i32, [i32; 2]> = HashMap::new();
    for i in 0..=9 {
        all_nodes.insert(i, [0, 0]);
    }
    let mut all_tail_pos: HashSet<[i32; 2]> = HashSet::new();

    for line in data {
        let (direction, repeat_str) = line.split_at(1);
        let repeat_int = repeat_str.trim().parse::<i32>();
        for _ in 0..=(repeat_int.unwrap() - 1) {
            for node_idx in 0..=(all_nodes.len() - 1) {
                let idx = node_idx as i32;
                let mut node_coords = *all_nodes.get(&idx).unwrap();

                if idx == 0 {
                    let mut new_pos = get_move_offset(direction);
                    new_pos[0] += node_coords[0].clone();
                    new_pos[1] += node_coords[1].clone();

                    all_nodes.insert(idx, new_pos);
                } else {
                    let diff_x = all_nodes[&(idx - 1)][0] - node_coords[0];
                    let diff_y = all_nodes[&(idx - 1)][1] - node_coords[1];
                    if (diff_x.abs() + diff_y.abs()) > 2 {
                        node_coords[0] += if diff_x > 0 { 1 } else { -1 };
                        node_coords[1] += if diff_y > 0 { 1 } else { -1 };
                    } else if diff_x.abs() > 1 {
                        node_coords[0] += if diff_x > 0 { 1 } else { -1 };
                    } else if diff_y.abs() > 1 {
                        node_coords[1] += if diff_y > 0 { 1 } else { -1 };
                    }

                    all_nodes.insert(idx, node_coords);

                    if node_idx == 9 {
                        all_tail_pos.insert(node_coords.clone());
                    }
                }
            }
        }
    }
    all_tail_pos.len() as i32
}

pub fn run(lines: &Vec<String>) {
    println!("part 1 {}", p1(lines));
    println!("part 2 {}", p2(lines));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1() {
        let expected_data = 13;
        let test_data: Vec<String> = vec!["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
            .iter()
            .map(|x| x.to_string())
            .collect();

        let res = p1(&test_data);
        assert_eq!(res, expected_data);
    }
}
