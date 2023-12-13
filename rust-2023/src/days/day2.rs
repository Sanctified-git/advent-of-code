use rust_utils::utils;
use regex::Regex;
use core::cmp::max;

fn check_games() {
	let input = utils::get_input(file!(), None);
	let mut part_one_sum = 0;
	let mut part_two_sum = 0;
	let re_r = Regex::new(r"(\d+) red").unwrap();
	let re_g = Regex::new(r"(\d+) green").unwrap();
	let re_b = Regex::new(r"(\d+) blue").unwrap();
	
	// PART ONE
	let mut game_index = 1;
	let (r_max, g_max, b_max) = (12, 13, 14);
	for mut l in input.clone() {
		let (_, rounds) = l.split_once(": ").unwrap();
		let (mut red, mut green, mut blue);
		let mut possible = true;
		for round in rounds.split("; ") {
			match re_r.captures(round) {
				Some(caps) => { red = i32::from_str_radix(&caps[1], 10).unwrap(); }
				None => { red = 0; }
			}
			match re_g.captures(round) {
				Some(caps) => { green = i32::from_str_radix(&caps[1], 10).unwrap(); }
				None => { green = 0; }
			}
			match re_b.captures(round) {
				Some(caps) => { blue = i32::from_str_radix(&caps[1], 10).unwrap(); }
				None => { blue = 0; }
			}
			if red > r_max || green > g_max || blue > b_max {
				possible = false;
				break
			}
		}
		if possible { part_one_sum += game_index }
		game_index += 1;
	}

	println!("The sum of calibration values is {}", part_one_sum);

	// PART TWO
	for mut l in input {
		let (_, rounds) = l.split_at_mut(8);
		let (mut r_min, mut g_min, mut b_min) = (1, 1, 1);
		for round in rounds.split("; ") {
			match re_r.captures(round) {
				Some(caps) => {
					let value = i32::from_str_radix(&caps[1], 10).unwrap(); 
					r_min = max(r_min, value)
				}
				None => {}
			}
			match re_g.captures(round) {
				Some(caps) => {
					let value = i32::from_str_radix(&caps[1], 10).unwrap();
					g_min = max(g_min, value)
				}
				None => {}
			}
			match re_b.captures(round) {
				Some(caps) => {
					let value = i32::from_str_radix(&caps[1], 10).unwrap();
					b_min = max(b_min, value)
				}
				None => {}
			}
		}
		part_two_sum += r_min * g_min * b_min;
	}

	println!("The new sum of calibration values is {}", part_two_sum);
}

/// https://adventofcode.com/2023/day/2
pub fn main() {
	let t = utils::build_timer(file!());
	check_games();
	t.step(file!());
}
