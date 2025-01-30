import sys
import math

def main():
    try:
        # Check if all arguments are provided
        if len(sys.argv) < 4:
            print("<p>Error: Missing input values. Please provide values for a, b, and c.</p>")
            sys.exit(1)

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
           
            c_cubed = c ** 3
            if c_cubed > 1000:
                final_result = math.sqrt(c_cubed) * 10
            else:
                final_result = math.sqrt(c_cubed) / a
            
            final_result += b
            result_message += f"<p>Final Result: {final_result:.2f}</p>"

        # Output the result as HTML
        print(result_message)

    except ValueError:
        print("<p>Error: Input values must be numeric.</p>")
    except Exception as e:
        print(f"<p>Error: {str(e)}</p>")

if __name__ == "__main__":
    main()