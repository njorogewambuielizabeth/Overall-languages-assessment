//  5. Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.


class Product(val name: String, val price: Double, val quantity: Int) {
    fun calculateTotalValue(): Double {
        return price * quantity
    }
}

fun main() {
    val product1 = Product("Apple", 1.5, 10)
    val product2 = Product("Banana", 0.75, 8)
    val product3 = Product("Orange", 1.25, 12)

    val totalValue1 = product1.calculateTotalValue()
    val totalValue2 = product2.calculateTotalValue()
    val totalValue3 = product3.calculateTotalValue()

    println("Total value of ${product1.name}s: $$totalValue1")
    println("Total value of ${product2.name}s: $$totalValue2")
    println("Total value of ${product3.name}s: $$totalValue3")

    val totalValueAll = totalValue1 + totalValue2 + totalValue3
    println("Total value of all products: $$totalValueAll")
}

# 6. Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
#  class student, get the sum grades then to get average divide by the total no of grades
# if averagegrade >=60 the student has passed

data class Student(val name: String, val age: Int, val grades: List<Int>) {
    fun calculateAverageGrade(): Double {
        val totalGrades = grades.sum()
        return totalGrades.toDouble() / grades.size
    }

    fun displayStudentInfo() {
        println("Name: $name")
        println("Age: $age")
        println("Grades: $grades")
    }

    fun hasPassed(): Boolean {
        val averageGrade = calculateAverageGrade()
        return averageGrade >= 60
    }
}

fun main() {
    val student1 = Student("Elizabeth", 21, listOf(80, 75, 90, 95))
    student1.displayStudentInfo()
    val averageGrade1 = student1.calculateAverageGrade()
    println("Average Grade: $averageGrade1")
    println("Passed: ${student1.hasPassed()}")

    println()

  
}

