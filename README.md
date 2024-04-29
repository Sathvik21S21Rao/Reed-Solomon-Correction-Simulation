## Reed-Solomon Simulation Overview

The Reed-Solomon simulation emulates a coding scheme widely used in error correction and data transmission applications. It operates based on Reed-Solomon codes, which are a class of error-correcting codes used for data transmission over noisy channels, such as in satellite communication, digital television, and storage systems like CDs, DVDs, and Blu-ray discs.

### How Reed-Solomon Codes Work

Reed-Solomon codes add redundancy to transmitted data, enabling the receiver to detect and correct errors. This redundancy is achieved by adding extra symbols to the original message before transmission. These extra symbols are computed based on the original message using polynomial operations.

### Simulation Components

1. **Global Setup**: Before transmitting data, the simulation requires global setup parameters, including the probability of error (`u`) and the size of the message space (`M`).

2. **Data Transmission**:
   - The `ReedSolomonSend` method is used to transmit data. It takes the original message as input and generates additional redundant symbols based on Reed-Solomon encoding techniques.
   - Randomness is introduced to simulate noise in the transmission process, affecting a subset of symbols.

3. **Data Recovery**:
   - The `ReedSolomonReceive` method is used to recover the transmitted message. It employs decoding techniques based on Reed-Solomon codes to correct errors introduced during transmission and reconstruct the original message.
   - Thue's algorithm is used to solve linear Diophantine equations, which are instrumental in error correction.

### Importance of Reed-Solomon Simulation

Reed-Solomon codes are essential in scenarios where reliable data transmission is crucial, especially in environments prone to noise and interference. By adding redundancy and employing sophisticated decoding techniques, Reed-Solomon codes ensure robustness and accuracy in data transmission, making them indispensable in various real-world applications.


## Project Structure

The project is organized into several Python modules:

1. **HelperFunctions Directory**
    - **arithmeticOps.py**: Contains various arithmetic operations such as modulo, power, division, logarithm, etc.
    - **BEGCD.py**: Implements the Binary Extended Greatest Common Divisor (BEGCD) algorithm.
    - **CRT.py**: Implements the Chinese Remainder Theorem (CRT) for large integers.
    - **MR2.py**: Implements the Miller-Rabin primality test for generating random primes.
    - **Thues.py**: Implements Thue's algorithm for finding solutions to linear Diophantine equations.
   
2. **ReedSolomon.py**: The main module that orchestrates the Reed-Solomon simulation. It imports functionalities from other modules to simulate data transmission and recovery.

## Functionality Overview

### Arithmetic Operations (arithmeticOps.py)
- **Modn**: Computes x mod n.
- **removeFactorOf2**: Finds the highest power of 2 that divides a number.
- **power**: Computes x raised to the power of n.
- **powerModN**: Computes x raised to the power of n modulo m.
- **division**: Performs integer division.
- **log2**: Computes the base-2 logarithm of a number.

### BEGCD (BEGCD.py)
- **begcd**: Implements the Binary Extended Greatest Common Divisor (BEGCD) algorithm.

### CRT (CRT.py)
- **CRT**: Implements the Chinese Remainder Theorem (CRT) for solving systems of congruences.

### MR2 (MR2.py)
- **Primality**: Implements the Miller-Rabin primality test for generating random primes.

### Thue's Algorithm (Thues.py)
- **thue**: Implements Thue's algorithm for finding solutions to linear Diophantine equations.

### Reed-Solomon Simulation (ReedSolomon.py)
- **ReedSolomonSimulation**: Orchestrates the Reed-Solomon simulation, including global setup, data transmission, and recovery.

## Usage Instructions

To use the Reed-Solomon simulation:

1. Ensure all required Python modules are installed, especially `gmpy2`.
2. Import the `ReedSolomonSimulation` class from `ReedSolomon.py`.
3. Initialize the simulation by calling the `GlobalSetup` method with the desired parameters (`u`, `M`).
4. Use the `ReedSolomonSend` method to transmit data by providing the message as input.
5. Call the `ReedSolomonReceive` method to receive the transmitted message. This method returns the recovered message.

## Running the Reed-Solomon Simulation

### Prerequisites
- **Python**: Make sure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).
- **Dependencies**: The simulation relies on the `gmpy2` library. Install it using pip:


### Steps
1. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory containing the Reed-Solomon simulation file (`ReedSolomon.py`).

2. **Run the File**: Execute the simulation file using the Python interpreter:


3. **Follow the Instructions**: The simulation will prompt you to enter a number to send. Enter the desired number and press Enter.

4. **View the Output**: If the simulation successfully recovers the message, it will display the received message. If not, it will indicate that the message could not be recovered.

# Contributors

- Shreyas
- Sathvik



Example Usage:
```python
from ReedSolomon import ReedSolomonSimulation

rs = ReedSolomonSimulation()
rs.GlobalSetup(0.3, 10**10)  # Setting up global parameters

# Transmitting data
rs.ReedSolomonSend(int(input("Enter number to send:")))

try:
    print("Received message is", rs.ReedSolomonReceive())  
except Exception as e:
    print("Could not recover message")
