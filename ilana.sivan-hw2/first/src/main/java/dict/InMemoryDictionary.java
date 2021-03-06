package dict;

import java.util.Map.Entry;
import java.io.*;
import java.util.TreeMap;


/**
 * Implements a persistent dictionary that can be held entirely in memory.
 * When flushed, it writes the entire dictionary back to a file.
 * <p>
 * The file format has one keyword per line:
 * <pre>word:def1:def2:def3,...</pre>
 * <p>
 * Note that an empty definition list is allowed (in which case the entry would have the form: <pre>word:</pre>
 *
 * @author talm
 */
public class InMemoryDictionary extends TreeMap<String, String> implements PersistentDictionary {
    private static final long serialVersionUID = 1L; // (because we're extending a serializable class)
    private File dictFile;

    public InMemoryDictionary(File dictFile) {
        this.dictFile = dictFile;
    }

    @Override
    public void open() throws IOException {

        FileReader myReader = null;
        BufferedReader myBR = null;
        String myLine, word, definition;
        int colon;
        try {
            // cleans the map.
            clear();
            // starts a new buffered reader to read the lines.
            myReader = new FileReader(dictFile);
            myBR = new BufferedReader(myReader);
            myLine = myBR.readLine();
            while (myLine != null) {
                // marks where the definition starts.
                colon = myLine.indexOf(":");
                if (colon != -1) {
                    // takes out the word and definition.
                    word = myLine.substring(0, colon);
                    definition = myLine.substring(colon + 1, myLine.length());
                    // saves the word and definition into the map.
                    put(word, definition);
                }
                myLine = myBR.readLine();
            }
        } catch (IOException e) {
            System.out.println("Dictionary doesn't exist");
        } finally {
            // closes loose ends.
            if (myBR != null) {
                myBR.close();
            }
            if (myReader != null) {
                myReader.close();
            }
        }

    }

    @Override
    public void close() throws IOException {

        FileWriter myWriter = null;
        String word, definition;
        try {
            // initialize writer
            myWriter = new FileWriter(dictFile);

            // run for every entry
            for (Entry<String, String> entry : entrySet()) {

                // get word and definition
                word = entry.getKey();
                definition = entry.getValue();

                // write a line
                myWriter.write(word + ":" + definition + "\n");
            }
        } catch (IOException e) {
            System.out.println("The file has an issue");
        } finally {
            // closes loose ends.
            myWriter.close();
        }
    }

}
