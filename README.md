## Nepal Local Governments

This is a simple package to get a list of local levels in Nepal (Rural Municipality,  Municipality and Metropolitian City) based on a given Province number/name or District name.

## Installation

You can install the package from PyPI using pip:
```
pip install neplocalgov
```
## Usage
The package contains only two simple functions  shown below

```
from neplocalgov import by_province, by_district

print(by_province(province="1")
print(by_district(district="Kathmandu")
```
If the supplied province / district is not valid, it returns Null. If data is found, it is returned as a list of dictionaries

## Contributions

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT LICENSE.

## Contact

For any queries or feedback, please contact [Shalin Devkota](mailto:youremail@example.com).