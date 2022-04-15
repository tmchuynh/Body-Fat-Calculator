## Body-Fat-Calculator

### [U.S. Navy Method](https://www.omnicalculator.com/health/navy-body-fat)
The calculator uses a method involving equations developed at the Naval Health Research Center by Hodgdon and Backett in 1984. The method for measuring the relevant body parts as well as the specific equations used are provided:

Note: If you are interested, there is also the [Army Body Fat Calculator](https://www.omnicalculator.com/health/army-body-fat)

- Measure the circumference of the subject's wasist at a horizontal level around the navel for **men**, and at the level with the smallest width for **women**. Ensure that the subject does not pull their stomach inwards.
- Measure the circumference of the subject's neck starting below the larynx, with the tape cloping downwards to the front. The subject should avoid flaring their neck outwards.
- **For women only**: Measure the circumference of the subject's hips at the largest horizontal measure

Once these measurements are obtained, in inches, the program will use the equations to calculate the body fat percentage for males and females respectively. 

Body fat percentage formula for females:

USC Units:
```
BFP = 163.205 × log10(waist + hip - neck) - 97.684×( log10(height) ) - 78.387
```
SI, Metric Unites:
```
BFP = 495 / (1.29579 - 0.35004 × log10(waist + hip - neck) + 0.22100 × log10(height) ) - 450
```

Body fat percentage formula for males:
```
BFP = 86.010 × log10(abdomen - neck) - 70.041 × log10(height) + 36.76
```
SI, Metric Unites:
```
BFP =	495 / ( 1.0324 - 0.19077 × log10(waist - neck) ) + 0.15456 × log10(height) )  - 450
```
Note: This program will be using the BMI method (for adults) as explained below:

### BMI Method
Another method for calculating an estimate of body fat percentage uses BMI, which takes in a person's height and weight. Given the respective data, the following formulas can be used to estimate an adult body's fat percentage:

Body fat percentage formula for adult females:
```
BFP = 1.20 * BMI + 0.23 * Age - 5.4
```

Body fat percentage formula for adult males:
```
BFP = 1.20 * BMI + 0.23 * Age - 16.2
```

### [Calculating BMI](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html)
Below are the equations used for calculating BMI:

USC Units:
```
BMI = 703 * ( mass in lbs / height in inches ^ 2 )
```

SI, Metric Units:
```
BMI = ( mass in kg / height in m ^ 2 )
```

### [Ponderal Index](https://www.calculator.net/bmi-calculator.html)
The Ponderal Index (PI) is similar to BMI and measures the leanness of corpulence of a person based on their height and weight. The main difference between the two is the subing rather than squaring of the height in the formula. While BMI is useful when considering large populations, it is not reliable for determining leanness in individuals. The PI is considered more reliable for use with very tall or short individuals while BMI tends to record uncharacteristically high or low body fat levels for those on extreme ends of the height and weight spectrum.

USC Units:
```
PI = ( height in inches / square root( mass in lbs ) )
```

SI, Metric Units:
```
PI = ( mass in kg / height in m ^ 3 )
```

### The American Council on Exercise Body Fat Categorization
| Description     | Women | Men |
| ----------- | ----------- | ----------- |
| Essential fat      | 	10-13%       | 2-5%       |
| Athletes   | 	14-20%        | 6-13%        |
| Fitness   | 21-24%        | 	14-17%        |
| Average   | 25-31%        | 	18-24%        |
| Obese   | 32+%        | 	25+%        |

### Body Fat, Overweight, and Obesity
The scientific term for body fat is "adipose tissue". Adipose tissue serves as a number of important functions in your body including creating energy, secreting a number of important hormones, and providing the body with cushioning and insulation. The healthy range of body fat for men is typically defined as 8-19% while the healthy range for women is 21-33%.

Excess body fat leads to the condition of being overweight and eventually to obesity given that insufficient measures are taken. Note: overweight does not necessarily mean an excess of body fat. 