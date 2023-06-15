//  5. Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

class Product {
    constructor(name, price, quantity) {
      this.name = name;
      this.price = price;
      this.quantity = quantity;
    }
  
    calculateTotalValue() {
      return this.price * this.quantity;
    }
  }
  
  // Example usage
  const product1 = new Product("Apple", 1.5, 10);
  const product2 = new Product("Banana", 0.75, 8);
  const product3 = new Product("Orange", 1.25, 12);
  
  const totalValue1 = product1.calculateTotalValue();
  const totalValue2 = product2.calculateTotalValue();
  const totalValue3 = product3.calculateTotalValue();
  
  console.log(`Total value of ${product1.name}s: $${totalValue1}`);
  console.log(`Total value of ${product2.name}s: $${totalValue2}`);
  console.log(`Total value of ${product3.name}s: $${totalValue3}`);
  
  const totalValueAll = totalValue1 + totalValue2 + totalValue3;
  console.log(`Total value of all products: $${totalValueAll}`);

//   6. Implement a class called Student with attributes for name, age, and grades (a
//     list of integers). Include methods to calculate the average grade, display the
//     student information, and determine if the student has passed (average grade >=
//     60). Create objects for the Student class and demonstrate the usage of these
//     methods.

// #  class student, get the sum grades then to get average divide by the total no of grades
// # if averagegrade >=60 the student has passed
class Student {
    constructor(name, age, grades) {
      this.name = name;
      this.age = age;
      this.grades = grades;
    }
   
    calculateAverageGrade() {
      const totalGrades = this.grades.reduce((acc, grade) => acc + grade, 0);
      const averageGrade = totalGrades / this.grades.length;
      return averageGrade;
    }
  
    displayStudentInfo() {
      console.log(`Name: ${this.name}`);
      console.log(`Age: ${this.age}`);
      console.log(`Grades: ${this.grades}`);
    }
  
    hasPassed() {
      const averageGrade = this.calculateAverageGrade();
      return averageGrade >= 60;
    }
  }
  
  const student1 = new Student("Elizabeth", 21, [80, 75, 90, 95]);
  student1.displayStudentInfo();
  const averageGrade1 = student1.calculateAverageGrade();
  console.log(`Average Grade: ${averageGrade1}`);
  console.log(`Passed: ${student1.hasPassed()}`);
  
  console.log();
  

  
  