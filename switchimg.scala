import java.io.{File, PrintWriter}
import scala.io._
import java.io.File

object switchimg {
	def main(args: Array[String]): Unit = {
		print("输入文件名：")
		val filename:String = StdIn.readLine()
		val curFilePath = "/Users/caiyiming/Downloads/"+filename+"/"+filename+".md"
		val targetFilePath = "/Users/caiyiming/myblog/source/_posts/"+filename+".md"

		val writer = new PrintWriter(new File(targetFilePath))
		writer.flush()

		val fileReader = Source.fromFile(curFilePath)

		writer.println("---")
		writer.println("title: "+filename+"\n\n\n")

		for(line <- fileReader.getLines()){
			if(line.indexOf("![](") == -1){
				writer.println(line)
			}else{
				val temp = line.replaceAll("image/","https://jktql.oss-cn-shanghai.aliyuncs.com/article/"+filename+"/")
				writer.println(temp)
			}
		}

		writer.close()
	}

}
