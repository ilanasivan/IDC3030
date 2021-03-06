package files;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

public class Streams {
    /**
     * Read from an InputStream until a quote character (") is found, then read
     * until another quote character is found and return the bytes in between the two quotes.
     * If no quote character was found return null, if only one, return the bytes from the quote to the end of the stream.
     *
     * @param in
     * @return A list containing the bytes between the first occurrence of a quote character and the second.
     */

    public static List<Byte> getQuoted(InputStream in) throws IOException {
        ArrayList<Byte> list = new ArrayList();
        boolean ifQuote = false;

        for (int i = in.read(); i >= 0; i = in.read()) {
            if (ifQuote) {
                // bytes
                if (i == 34) {
                    break;
                }

                list.add((byte) i);
            } else if (i == 34) {
                ifQuote = true;
            }
        }

        return ifQuote ? list : null;
    }


    /**
     * Read from the input until a specific string is read, return the string read up to (not including) the endMark.
     *
     * @param in      the Reader to read from
     * @param endMark the string indicating to stop reading.
     * @return The string read up to (not including) the endMark (if the endMark is not found, return up to the end of the stream).
     */
    public static String readUntil(Reader in, String endMark) throws IOException {
        // initialize
        StringBuilder str = new StringBuilder();

        // iterate
        for (int i = in.read(); i >= 0; i = in.read()) {

            // append to new string
            str.append((char) i);

            // check if we have a stop
            if (str.toString().endsWith(endMark)) {

                // return string before the end mark not including it
                return str.substring(0, str.length() - endMark.length());
            }
        }

        return str.toString();
    }

    /**
     * Copy bytes from input to output, ignoring all occurrences of badByte.
     *
     * @param in
     * @param out
     * @param badByte
     */
    public static void filterOut(InputStream in, OutputStream out, byte badByte) throws IOException {
//		iterate through and filter
        for (int i = in.read(); i >= 0; i = in.read()) {

            // check if i is badByte (given)
            if ((byte) i != badByte) {
                out.write(i);
            }
        }
    }

    /**
     * Read a 40-bit (unsigned) integer from the stream and return it. The number is represented as five bytes,
     * with the most-significant byte first.
     * If the stream ends before 5 bytes are read, return -1.
     *
     * @param in
     * @return the number read from the stream
     */
    public static long readNumber(InputStream in) throws IOException {
        // initialize long with literal and store value to it
        long myNum = 0L;


        // iterate
        // If the stream ends before 5 bytes are read, the method should return -1
        for (int i = 0; i < 5; ++i) {
            int j = in.read();
            if (j < 0) {
                // return if we end before 5 bytes
                return -1L;
            }

            // bit wise shift
            myNum <<= 8;
            // who will win, one lonely boy or my pipe
            myNum |= (long) j;
        }
        return myNum;
    }
}




