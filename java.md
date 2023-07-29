# Java



## Installing Java

```
[thor@app01 ~]$ sudo curl https://download.java.net/java/GA/jdk20/bdc68b4b9cbc4ebcb30745c85038d91d/36/GPL/openjdk-20_linux-x64_bin.tar.gz --output /opt/openjdk-20_linux-x64_bin.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  188M  100  188M    0     0  60.2M      0  0:00:03  0:00:03 --:--:-- 60.2M


[thor@app01 ~]$ ls -l /opt
total 192936
-rw-r--r-- 1 root root 197562076 Jul 29 14:23 openjdk-20_linux-x64_bin.tar.gz

[thor@app01 ~]$ sudo tar -xf /opt/openjdk-20_linux-x64_bin.tar.gz -C /opt/

[thor@app01 ~]$ ls -l /opt
total 192940
drwxr-xr-x 8 root root      4096 Jul 29 14:24 jdk-20
-rw-r--r-- 1 root root 197562076 Jul 29 14:23 openjdk-20_linux-x64_bin.tar.gz


[thor@app01 ~]$ /opt/jdk-20/bin/java -version
openjdk version "20" 2023-03-21
OpenJDK Runtime Environment (build 20+36-2344)
OpenJDK 64-Bit Server VM (build 20+36-2344, mixed mode, sharing)
[thor@app01 ~]$ 
```

## Adding java binary to PATH

```
[thor@app01 ~]$ vi .bash_profile 
[thor@app01 ~]$ cat .bash_profile 
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/.local/bin:$HOME/bin:/opt/jdk-20/bin/

export PATH

[thor@app01 ~]$ source .bash_profile 
[thor@app01 ~]$ java -version
openjdk version "20" 2023-03-21
OpenJDK Runtime Environment (build 20+36-2344)
OpenJDK 64-Bit Server VM (build 20+36-2344, mixed mode, sharing)
```


### Important Notes

- JDK is Java Development it
- Before Java version 9, versions were like 1.8, 1.6, 1.4, 1.3... After java 9 they changed the name convension 
- Java 1.8.x is actually Java version 8.x
- Javadoc is used to documment your App with JDK
- Javac is used for compiling your app with JDK
- jdb is used for debugging your app
- Before Java 9 JDK and JRE was installed a part, noadays we install JDK and JRE is part of the package


### Java lifecycle 

1. Develop Code
2. Compile
3. Run

#### Compiling example

```
$ javac MyClass.java
```

#### Running java app

```
$ java MyClass
```

This is the name of the class coded within MyClass.java


### Package


- When we have may .class files we can create a JAR (Java Archive)
    - MyClass.class
    - Service1.class
    - Service2.class

In case of web page we may have WAR (Web Archive)

```
$ jar cf MyApp.jar MyClass.class Service1.class Service2.class...
MyApp.jar
```

- meta-inf/manifest.mf is the manifest file


### Document

```
$ javadoc -d doc MyClass.java
```


### Build Process

1. Develop
2. Compile -> `javac MyClass.java`
3. Package -> `jar cf MyClass.jar ...`
4. Document -> `javadoc MyClass.java`


### Build Tools

- Maven
- Gradle
- Ant


- Build Steps

1. Compile
2. Package
3. Document


#### Ant

```
javac MyClass.java
javadoc MyClass.java
jar cf MyClass.jar...
```


```
ant compile jar
```

This ant command will get the configuration build.xml file that we need created within the directory. This `build.xml` file will have those two sessions called `compile` and `jar`


## Java Code

```
thor@host01 /opt/app$ cat MyClass.java 
/**
 * Prints Hello World Message
 *
 */

public class MyClass {
    
    /**
     * Default constructor for the MyClass class.
     */

    public MyClass() {
    }

    /**
     * The main method that prints the message.
     *
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Hello Kodekloud");
    }
}
```


### Compiling MyClass.java

```
thor@host01 /opt/app$ javac MyClass.java 
thor@host01 /opt/app$ ls
MyClass.class  MyClass.java
thor@host01 /opt/app$ 
```

### Running a Java application

```
thor@host01 /opt/app$ java MyClass
Hello Kodekloud
```

### Generating documentation


```
thor@host01 /opt/app$ javadoc -d doc MyClass.java 
Loading source file MyClass.java...
Constructing Javadoc information...
Creating destination directory: "doc/"
Building index for all the packages and classes...
Standard Doclet version 20.0.1+9-29
Building tree for all the packages and classes...
Generating doc/MyClass.html...
Generating doc/package-summary.html...
Generating doc/package-tree.html...
Generating doc/overview-tree.html...
Building index for all classes...
Generating doc/allclasses-index.html...
Generating doc/allpackages-index.html...
Generating doc/index-all.html...
Generating doc/search.html...
Generating doc/index.html...
Generating doc/help-doc.html...

thor@host01 /opt/app$ ls
doc  MyClass.class  MyClass.java
```


### Installing ANT


```
$ sudo yum install -y ant
```

```
thor@host01 /opt/ant$ ls
build  build.xml  dist  docs  src

thor@host01 /opt/ant$ cat build.xml 
<?xml version="1.0"?>
<project name="Ant" default="main" basedir=".">
    <!-- Compiles the java code (including the usage of library for JUnit -->
    <target name="compile">
        <javac srcdir="/opt/ant/src" destdir="/opt/ant/build">
        </javac>
    </target>
    <!-- Creates Javadoc -->
    <target name="docs" depends="compile">
        <javadoc packagenames="src" sourcepath="/opt/ant/src" destdir="/opt/ant/docs">
            <!-- Define which files / directory should get included, we include all -->
            <fileset dir="/opt/ant/src">
                <include name="**" />
            </fileset>
        </javadoc>
    </target>
    <!--Creates the deployable jar file  -->
    <target name="jar" depends="compile">
        <jar basedir="/opt/ant/build" destfile="/opt/ant/dist/MyClass.jar" >
            <manifest>
                <attribute name="Main-Class" value="MyClass" />
            </manifest>
        </jar>
    </target>
    <target name="run" depends="jar">
      <java jar="/opt/ant/dist/MyClass.jar" fork="true" />
    </target>
    <target name="main" depends="compile, jar, docs, run">
        <description>Main target</description>
    </target>
</project>
```



### Using ANT to compile and genarate jar package

```
thor@host01 /opt/ant$ ant compile jar
Buildfile: /opt/ant/build.xml

compile:
    [javac] /opt/ant/build.xml:5: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 1 source file to /opt/ant/build

compile:
    [javac] /opt/ant/build.xml:5: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds

jar:
      [jar] Building jar: /opt/ant/dist/MyClass.jar

BUILD SUCCESSFUL
Total time: 0 seconds
```

### Running ANT for all steps in `/opt/ant/build.xml`

```
thor@host01 /opt/ant$ ant
Buildfile: /opt/ant/build.xml

compile:
    [javac] /opt/ant/build.xml:5: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds

jar:

docs:
  [javadoc] Generating Javadoc
  [javadoc] Javadoc execution
  [javadoc] Loading source file /opt/ant/src/MyClass.java...
  [javadoc] Constructing Javadoc information...
  [javadoc] Standard Doclet version 1.8.0_372
  [javadoc] Building tree for all the packages and classes...
  [javadoc] Building index for all the packages and classes...
  [javadoc] Building index for all classes...

run:
     [java] Hello Kodekloud

main:

BUILD SUCCESSFUL
Total time: 0 seconds
```


## Installing Maven

```
$ sudo yum install -y maven
```


```
thor@host01 /opt/maven/my-app$ tree
.
├── pom.xml
└── src
    ├── main
    │   └── java
    │       └── com
    │           └── mycompany
    │               └── app
    │                   └── App.java
    └── test
        └── java
            └── com
                └── mycompany
                    └── app
                        └── AppTest.java

11 directories, 3 files
```

### Compiling and package with Maven

```
thor@host01 /opt/maven/my-app$ sudo mvn package
[INFO] Scanning for projects...
[INFO]                                                                         
[INFO] ------------------------------------------------------------------------
[INFO] Building my-app 1.0-SNAPSHOT
[INFO] ------------------------------------------------------------------------
Downloading: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.pom
Downloaded: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.pom (7 KB at 25.3 KB/sec)
Downloading: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/30/maven-plugins-30.pom
Downloaded: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/30/maven-plugins-30.pom (10 KB at 283.8 KB/sec)
Downloading: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.jar
Downloaded: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.jar (31 KB at 755.2 KB/sec)
Downloading: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.8.0/maven-compiler-plugin-3.8.0.pom
Downloaded: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.8.0/maven-compiler-plugin-3.8.0.pom (13 KB at 357.1 KB/sec)
Downloading: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/32/maven-plugins-32.pom
Downloaded: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/32/maven-plugins-32.pom (11 KB at 316.3 KB/sec)
Downloading: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/32/maven-parent-32.pom
Downloaded: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/32/maven-parent-32.pom (43 KB at 1175.5 KB/sec)
Downloading: https://repo.maven.apache.org/maven2/org/apache/apache/20/apache-20.pom
Downloaded: https://repo.maven.apache.org/maven2/org/apache/apache/20/apache-20.pom (16 KB at 442.3 KB/sec)
Downloading: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.8.0/maven-compiler-plugin-3.8.0.jar
Downloaded: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.8.0/maven-compiler-plugin-3.8.0.jar (61 KB at 1591.7 KB/sec)
...
[INFO] Building jar: /opt/maven/my-app/target/my-app-1.0-SNAPSHOT.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 6.739s
[INFO] Finished at: Sat Jul 29 15:36:05 UTC 2023
[INFO] Final Memory: 22M/1475M
[INFO] ------------------------------------------------------------------------
```


### Running java with maven package

```
thor@host01 /opt/maven/my-app/target$ java -cp /opt/maven/my-app/target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
Hello World!
```






