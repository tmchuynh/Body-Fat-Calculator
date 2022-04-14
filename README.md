## Body-Fat-Calculator

### U.S. Navy Method
The calculator uses a method involving equations developed at the Naval Health Research Center by Hodgdon and Backett in 1984. The method for measuring the relevant body parts as well as the specific equations used are provided:

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
Note: This program will be using the USC Units formula

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