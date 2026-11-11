package word;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.fs.Path;

public class KMeans {

    public static class Map extends Mapper<LongWritable, Text, IntWritable, IntWritable> {

        public void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {

            int point = Integer.parseInt(value.toString());

            int c1 = 10;
            int c2 = 50;

            int d1 = Math.abs(point - c1);
            int d2 = Math.abs(point - c2);

            if (d1 < d2)
                context.write(new IntWritable(1), new IntWritable(point));
            else
                context.write(new IntWritable(2), new IntWritable(point));
        }
    }

    public static class Reduce extends Reducer<IntWritable, IntWritable, IntWritable, IntWritable> {

        public void reduce(IntWritable key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException {

            int sum = 0, count = 0;

            for (IntWritable x : values) {
                sum += x.get();
                count++;
            }

            context.write(key, new IntWritable(sum / count));
        }
    }

    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();
        Job job = new Job(conf, "KMeans Clustering");

        job.setJarByClass(KMeans.class);
        job.setMapperClass(Map.class);
        job.setReducerClass(Reduce.class);

        job.setOutputKeyClass(IntWritable.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}




//commands to execute the program
wget --no-check-certificate http://raw.githubusercontent.com/arbazahmed07/wc/main/kmeans.sh
chmod +x kmeans.sh
bash kmeans.sh