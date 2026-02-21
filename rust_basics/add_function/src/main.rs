use std::io;

fn add(a: i32, b:i32) -> i32{
	a+b
}

fn main () {
	println!("Enter the first number");

	let mut x = String::new();
	io::stdin().read_line(&mut x).expect("Failed to injest the first number");
	let x: i32 = x.trim().parse().expect("Not a number");

	println!("Enter the second number");
	
	let mut y = String::new();
	io::stdin().read_line(&mut y).expect("Failed to injest the second number");
	let y: i32 = y.trim().parse().expect("Not a number");

	let sum = add(x, y);

	println!("The sum is {sum}");
}
