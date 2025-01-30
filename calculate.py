import sys
import math

def main():
    try:
        # Retrieve input values from command-line arguments
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])

        # Initialize result message
        result_message = ""

        # Conditional checks
        if a < 1:
            result_message += "<p>Input for 'a' is too small.</p>"
        if b == 0:
            result_message += "<p>Input for 'b' is 0 and will not affect the result.</p>"
        if c < 0:
            result_message += "<p>Error: Input for 'c' is negative.</p>"
        else:
            # Compute c^3
            c_cubed = c ** 3
            if c_cubed > 1000:
                final_result = math.sqrt(c_cubed) * 10
            else:
                final_result = math.sqrt(c_cubed) / a
            # Add b to the final result
            final_result += b
            result_message += f"<p>Final Result: {final_result:.2f}</p>"

        # Output the result as HTML
        print(result_message)

    except Exception as e:
        print(f"<p>Error: {str(e)}</p>")

if __name__ == "__main__":
    main()