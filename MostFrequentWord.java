
import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;

public class MostFrequentWord {

    // Mapper
    public static class TokenizerMapper
        extends Mapper<Object, Text, Text, IntWritable> {

        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();

        public void map(Object key, Text value, Context context)
            throws IOException, InterruptedException {

            StringTokenizer itr =
                new StringTokenizer(value.toString());

            while (itr.hasMoreTokens()) {
                word.set(itr.nextToken().toLowerCase());
                context.write(word, one);
            }
        }
    }

    // Reducer
    public static class IntSumReducer
        extends Reducer<Text, IntWritable, Text, IntWritable> {

        private Text maxWord = new Text();
        private int maxCount = 0;

        public void reduce(Text key, Iterable<IntWritable> values,
            Context context) throws IOException, InterruptedException {

            int sum = 0;

            for (IntWritable val : values) {
                sum += val.get();
            }

            if (sum > maxCount) {
                maxCount = sum;
                maxWord.set(key);
            }
        }

        // Final output
        protected void cleanup(Context context)
            throws IOException, InterruptedException {

            context.write(maxWord, new IntWritable(maxCount));
        }
    }

    // Main Method
    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();

        Job job = Job.getInstance(conf, "Most Frequent Word");

        job.setJarByClass(MostFrequentWord.class);

        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        // Single reducer for global maximum
        job.setNumReduceTasks(1);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}




//commands to execute the program

wget --no-check-certificate http://raw.githubusercontent.com/arbazahmed07/wc/main/freq.sh
chmod +x freq.sh
bash freq.sh