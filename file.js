const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageNumber, Footer, PageBreak, UnderlineType
} = require('docx');
const fs = require('fs');

const border = { style: BorderStyle.SINGLE, size: 1, color: "AAAAAA" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

function heading1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    bidirectional: true,
    spacing: { before: 360, after: 200 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "1F3864", space: 4 } },
    children: [
      new TextRun({
        text,
        font: "Arial",
        size: 32,
        bold: true,
        color: "1F3864",
        rtl: true,
      })
    ]
  });
}

function heading2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    bidirectional: true,
    spacing: { before: 280, after: 140 },
    children: [
      new TextRun({
        text,
        font: "Arial",
        size: 26,
        bold: true,
        color: "2E74B5",
        rtl: true,
      })
    ]
  });
}

function para(text, options = {}) {
  return new Paragraph({
    bidirectional: true,
    alignment: AlignmentType.RIGHT,
    spacing: { before: 80, after: 120, line: 360 },
    children: [
      new TextRun({
        text,
        font: "Arial",
        size: 24,
        rtl: true,
        bold: options.bold || false,
        color: options.color || "000000",
      })
    ]
  });
}

function bullet(text) {
  return new Paragraph({
    bidirectional: true,
    alignment: AlignmentType.RIGHT,
    numbering: { reference: "bullets", level: 0 },
    spacing: { before: 60, after: 60, line: 340 },
    children: [
      new TextRun({ text, font: "Arial", size: 23, rtl: true })
    ]
  });
}

function numbered(text) {
  return new Paragraph({
    bidirectional: true,
    alignment: AlignmentType.RIGHT,
    numbering: { reference: "numbers", level: 0 },
    spacing: { before: 60, after: 60, line: 340 },
    children: [
      new TextRun({ text, font: "Arial", size: 23, rtl: true })
    ]
  });
}

function emptyLine() {
  return new Paragraph({ children: [new TextRun("")], spacing: { before: 80, after: 80 } });
}

function sectionLabel(text) {
  return new Paragraph({
    bidirectional: true,
    alignment: AlignmentType.RIGHT,
    spacing: { before: 140, after: 80 },
    children: [
      new TextRun({
        text,
        font: "Arial",
        size: 24,
        bold: true,
        color: "C00000",
        rtl: true,
      })
    ]
  });
}

// Cover page
function coverPage() {
  return [
    emptyLine(), emptyLine(), emptyLine(),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      bidirectional: true,
      spacing: { before: 0, after: 80 },
      children: [new TextRun({ text: "بحث بعنوان", font: "Arial", size: 26, color: "555555", rtl: true })]
    }),
    emptyLine(),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      bidirectional: true,
      spacing: { before: 0, after: 120 },
      border: {
        bottom: { style: BorderStyle.DOUBLE, size: 6, color: "1F3864", space: 6 },
        top: { style: BorderStyle.DOUBLE, size: 6, color: "1F3864", space: 6 },
      },
      children: [
        new TextRun({
          text: "إنترنت السلوك (IoB)",
          font: "Arial",
          size: 56,
          bold: true,
          color: "1F3864",
          rtl: true,
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      bidirectional: true,
      spacing: { before: 80, after: 0 },
      children: [
        new TextRun({
          text: "Internet of Behaviors",
          font: "Arial",
          size: 36,
          bold: true,
          color: "2E74B5",
          italics: true,
        })
      ]
    }),
    emptyLine(), emptyLine(), emptyLine(), emptyLine(),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      bidirectional: true,
      children: [new TextRun({ text: "التطبيقات • النماذج • التحديات الأخلاقية • أسئلة المحاضرة", font: "Arial", size: 24, color: "444444", rtl: true })]
    }),
    emptyLine(), emptyLine(), emptyLine(), emptyLine(), emptyLine(),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "2025 - 2026", font: "Arial", size: 24, bold: true, color: "333333" })]
    }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

// Comparison table IoT vs IoB
function comparisonTable() {
  const headerShading = { fill: "1F3864", type: ShadingType.CLEAR };
  const oddShading = { fill: "EEF3FA", type: ShadingType.CLEAR };
  const evenShading = { fill: "FFFFFF", type: ShadingType.CLEAR };

  function headerCell(text) {
    return new TableCell({
      borders,
      shading: headerShading,
      width: { size: 4500, type: WidthType.DXA },
      margins: { top: 100, bottom: 100, left: 150, right: 150 },
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        bidirectional: true,
        children: [new TextRun({ text, font: "Arial", size: 24, bold: true, color: "FFFFFF", rtl: true })]
      })]
    });
  }

  function row(left, right, shade) {
    return new TableRow({
      children: [
        new TableCell({
          borders, shading: shade,
          width: { size: 4500, type: WidthType.DXA },
          margins: { top: 80, bottom: 80, left: 150, right: 150 },
          children: [new Paragraph({ alignment: AlignmentType.RIGHT, bidirectional: true, children: [new TextRun({ text: right, font: "Arial", size: 22, rtl: true })] })]
        }),
        new TableCell({
          borders, shading: shade,
          width: { size: 4500, type: WidthType.DXA },
          margins: { top: 80, bottom: 80, left: 150, right: 150 },
          children: [new Paragraph({ alignment: AlignmentType.RIGHT, bidirectional: true, children: [new TextRun({ text: left, font: "Arial", size: 22, rtl: true })] })]
        }),
      ]
    });
  }

  return new Table({
    width: { size: 9000, type: WidthType.DXA },
    rows: [
      new TableRow({
        children: [headerCell("إنترنت الأشياء (IoT)"), headerCell("إنترنت السلوك (IoB)")]
      }),
      row("يربط الأجهزة الفيزيائية بالإنترنت", "يجمع ويحلل البيانات السلوكية البشرية", { fill: "EEF3FA", type: ShadingType.CLEAR }),
      row("يجمع بيانات خام من البيئة", "يفسر ويتنبأ بالسلوك البشري ويؤثر عليه", { fill: "FFFFFF", type: ShadingType.CLEAR }),
      row("تركيزه: الأجهزة والاتصال", "تركيزه: الأشخاص وتغيير السلوك", { fill: "EEF3FA", type: ShadingType.CLEAR }),
      row("يجيب على: ماذا يحدث؟", "يجيب على: لماذا ومتى وكيف نغير السلوك؟", { fill: "FFFFFF", type: ShadingType.CLEAR }),
      row("مثال: ثرموستات ذكي يقيس درجة الحرارة", "مثال: ثرموستات يتعلم العادات ويوفر الطاقة", { fill: "EEF3FA", type: ShadingType.CLEAR }),
      row("IoT هي البنية التحتية والأساس", "IoB هو الذكاء المبني فوق IoT", { fill: "FFFFFF", type: ShadingType.CLEAR }),
    ]
  });
}

const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022",
          alignment: AlignmentType.RIGHT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } }
        }]
      },
      {
        reference: "numbers",
        levels: [{
          level: 0, format: LevelFormat.DECIMAL, text: "%1.",
          alignment: AlignmentType.RIGHT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } }
        }]
      },
    ]
  },
  styles: {
    default: {
      document: { run: { font: "Arial", size: 24 } }
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: "1F3864" },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: "2E74B5" },
        paragraph: { spacing: { before: 280, after: 140 }, outlineLevel: 1 }
      },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1440, right: 1800, bottom: 1440, left: 1800 }
      }
    },
    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 20, color: "777777" }),
            ]
          })
        ]
      })
    },
    children: [
      ...coverPage(),

      // ============ Q1 ============
      heading1("أولاً: تعريف إنترنت السلوك (IoB)"),
      para("إنترنت السلوك (Internet of Behaviors - IoB) هو إطار تكنولوجي يقوم على جمع البيانات المتعلقة بالسلوك البشري من الأجهزة المتصلة بالإنترنت، ثم تحليلها باستخدام الذكاء الاصطناعي وعلم البيانات وعلم النفس السلوكي، بهدف فهم السلوك البشري والتنبؤ به والتأثير عليه."),
      emptyLine(),
      para("صاغ هذا المصطلح الباحث G. Wayne Clough وأطلق عليه الانتشار الواسع شركة Gartner عام 2020 حين صنّفته ضمن أبرز التوجهات التكنولوجية الاستراتيجية."),
      emptyLine(),
      heading2("مكونات IoB الثلاثة"),
      bullet("التكنولوجيا: إنترنت الأشياء (IoT)، الذكاء الاصطناعي، البيانات الضخمة"),
      bullet("تحليل البيانات: تحديد الأنماط والتوقعات السلوكية"),
      bullet("علم السلوك: علم النفس وعلم الاجتماع لفهم دوافع الإنسان"),
      emptyLine(),
      heading2("مصادر البيانات الرئيسية"),
      bullet("الأجهزة القابلة للارتداء (Wearables) مثل الساعات الذكية"),
      bullet("الهواتف الذكية وتطبيقاتها"),
      bullet("الأجهزة المنزلية الذكية والمركبات"),
      bullet("منصات التواصل الاجتماعي وتاريخ التصفح"),
      bullet("بيانات الموقع الجغرافي GPS"),
      bullet("سجلات المشتريات الإلكترونية"),
      bullet("كاميرات المراقبة وأنظمة التعرف على الوجه"),
      emptyLine(),

      // ============ Q2 ============
      heading1("ثانياً: الفرق بين IoT وIoB"),
      para("إنترنت الأشياء (IoT) هو الأساس التقني لإنترنت السلوك؛ إذ يوفر البيانات الخام، بينما يضيف IoB طبقة التحليل السلوكي والتأثير. الفرق الجوهري:"),
      emptyLine(),
      comparisonTable(),
      emptyLine(),
      para("باختصار: IoT هو شبكة من المستشعرات التي ترصد العالم، أما IoB فهو العقل الذي يفسّر ما يراه ويقرر كيف يؤثر في السلوك البشري.", { color: "1F3864", bold: true }),
      emptyLine(),

      // ============ Q3: Nudging ============
      heading1("ثالثاً: الحث السلوكي (Nudging) في إنترنت السلوك"),
      para("الحث السلوكي (Nudge) هو تدخّل خفي وغير إلزامي يجعل السلوك المرغوب أسهل أو أكثر جاذبية دون تقييد حرية الاختيار. صاغه الاقتصادي Richard Thaler (الحائز على نوبل) وCass Sunstein في كتابهما الشهير."),
      emptyLine(),
      para("في سياق IoB، يُطوَّر الحث السلوكي ليكون مخصصاً لكل فرد بناءً على بياناته السلوكية الحقيقية، ومُقدَّماً في اللحظة المثلى للتأثير."),
      emptyLine(),
      heading2("أنواع الحث السلوكي في IoB مع أمثلة"),

      sectionLabel("1. التذكيرات الذكية في الوقت المناسب"),
      bullet("تطبيق اللياقة يرصد عبر GPS بقاءك جالساً 60 دقيقة في مكتبك، فيرسل تذكيراً بالمشي."),
      bullet("ساعة Apple Watch ترسل تنبيهاً لغسل اليدين عند دخول الحمام."),

      sectionLabel("2. المقارنة الاجتماعية (Social Proof)"),
      bullet("فاتورة الكهرباء تُظهر: 'استهلكتَ 20% أكثر من جيرانك' — تقلّل الاستهلاك فعلياً بنسبة 2-5%."),
      bullet("LinkedIn يُبيّن عدد الأشخاص الذين تقدموا لوظيفة ما لتحفيزك على التقديم السريع."),

      sectionLabel("3. الإعدادات الافتراضية (Default Settings)"),
      bullet("تطبيقات التقاعد تضع خصماً افتراضياً 5% على الراتب — نادراً ما يغيّره المستخدمون."),
      bullet("متجر أمازون يضع 'الشراء بنقرة واحدة' افتراضياً لتسهيل الشراء."),

      sectionLabel("4. التلعيب (Gamification)"),
      bullet("عداد التتابع (Streak) في Duolingo يستغل نفور الخسارة — المستخدم لا يريد كسر سلسلة أيامه."),
      bullet("حلقات النشاط في Apple Watch تدفع المستخدمين لإغلاقها يومياً."),

      sectionLabel("5. الشح والإلحاح (Scarcity & Urgency)"),
      bullet("'بقي عنصران فقط في المخزون!' — يستغل تحيز الندرة لتسريع قرار الشراء."),
      bullet("'3 أشخاص يشاهدون هذا المنتج الآن' — ضغط اجتماعي مؤتمت."),
      emptyLine(),

      // ============ Q4: Applications ============
      heading1("رابعاً: تطبيقات إنترنت السلوك بالأمثلة"),

      heading2("أ) التجارة الإلكترونية والتسوق"),
      para("يُعدّ IoB محرّك التوصيات في منصات التجارة الإلكترونية الكبرى:"),
      bullet("أمازون: محرك 'العملاء اشتروا أيضاً' يُولّد 35% من إيراداتها. يتتبع تاريخ التصفح، والنقرات، والعناصر المتروكة في السلة، وفترات التحديق في المنتج."),
      bullet("نون وسوق: تخصيص الصفحة الرئيسية والعروض بناءً على سجل البحث والشراء لكل مستخدم."),
      bullet("Zalando: يحلل سلوك التمرير والتصفح ليتنبأ بالمقاسات المفضلة ويُقلّل معدل الإرجاع."),
      bullet("Shopify: يُنبّه التجار عندما يتوقف مستخدم عن الشراء في منتصف الطريق ويرسل عروضاً استرداداً."),
      emptyLine(),

      heading2("ب) نمذجة السلوك (Behaviour Modelling) — نموذج تطبيقي"),
      para("نمذجة السلوك هي عملية بناء نموذج رياضي أو إحصائي يمثّل سلوك الأفراد بهدف التنبؤ بتصرفاتهم المستقبلية. تمر بأربع مراحل:"),
      numbered("جمع البيانات: تسجيل كل تفاعلات المستخدم (نقرات، مدة المشاهدة، التوقفات، إعادة التشغيل)."),
      numbered("تحليل الأنماط: تجميع المستخدمين في شرائح سلوكية متشابهة."),
      numbered("بناء النموذج: استخدام ML (Collaborative Filtering, Neural Networks) للتنبؤ بالسلوك التالي."),
      numbered("التدخّل: تقديم المحتوى أو الإجراء المناسب في اللحظة الصحيحة."),
      emptyLine(),
      para("مثال: Netflix يُحلّل معدلات الإيقاف، وإعادة المشاهدة، ووقت التشغيل المفضل، فيتنبأ بأي مسلسل ستضغط عليه بعد 10 ثوانٍ."),
      emptyLine(),

      heading2("ج) التمويل والبنوك"),
      bullet("التسجيل الائتماني السلوكي: يُحلّل كيفية تعامل المستخدم مع التطبيق البنكي (وقت الدخول، أنماط الإنفاق، انتظام السداد) لتقييم الجدارة الائتمانية."),
      bullet("التوفير التلقائي: تطبيق Digit يُحلّل الدخل والإنفاق ويحوّل مبالغ صغيرة للادخار تلقائياً دون أن يشعر المستخدم بثقلها."),
      bullet("الكشف عن الاحتيال: تُحلّل البنوك الأنماط السلوكية لرصد المعاملات غير المعتادة فوراً."),
      bullet("تأمين السيارات (Telematics): جهاز OBD يرصد الانعطافات، والكبح، والسرعة — السائقون الآمنون يحصلون على أقساط أقل."),
      emptyLine(),

      // ============ Q5: Human Decisions ============
      heading1("خامساً: كيف يدعم IoB القرارات البشرية ويشكّلها؟"),
      para("يعمل IoB على ثلاثة مستويات متدرجة في التأثير على القرار البشري:"),
      emptyLine(),

      sectionLabel("المستوى الأول: الإعلام (Inform)"),
      para("تقديم المعلومة الصحيحة في الوقت الصحيح لتحسين جودة القرار."),
      bullet("التطبيق الصحي يعرض منحنى سكر الدم لمريض السكري قبيل وجبته مباشرة — يساعده على اختيار الطعام الصحيح."),
      bullet("الثلاجة الذكية تُخطر بالمواد الغذائية قاربت على الانتهاء وتقترح وصفات مناسبة لها."),
      emptyLine(),

      sectionLabel("المستوى الثاني: الحث (Nudge)"),
      para("تقليل العوائق أمام الخيارات الجيدة دون إلزام أو منع."),
      bullet("التطبيق البنكي يُحوّل الفائض تلقائياً إلى الادخار في اليوم التالي لصرف الراتب — حين يكون المستخدم أقل احتمالاً للاعتراض."),
      bullet("تطبيق التأمين الصحي يرسل تذكيراً بموعد الطبيب السنوي بناءً على سجل الزيارات السابقة."),
      emptyLine(),

      sectionLabel("المستوى الثالث: تشكيل السلوك طويل الأمد (Shape)"),
      para("التدخلات المتكررة تُكوّن عادات جديدة وتُعيد برمجة السلوك."),
      bullet("أجهزة تتبع النشاط تربط المشي بالمكافآت — يتشكّل تدريجياً سلوك ممارسة الرياضة يومياً."),
      bullet("نظام الائتمان الاجتماعي الصيني يرصد سلوكيات المواطنين (مخالفات المرور، المشتريات، النشاط الرقمي) ويُسند لكل مواطن درجة تؤثر على وصوله للقروض والسفر — تشكيل سلوك مجتمعي شامل."),
      emptyLine(),

      // ============ Q6: Ethics ============
      heading1("سادساً: التحديات الأخلاقية لإنترنت السلوك"),
      para("يُثير IoB تساؤلات عميقة حول الخصوصية والاستقلالية والسلطة. فيما يلي أبرز ستة تحديات أخلاقية:"),
      emptyLine(),

      sectionLabel("1. انتهاك الخصوصية"),
      para("يتطلب IoB جمع بيانات ضخمة عن أدق تفاصيل الحياة اليومية: الموقع، الصحة، المشاعر، العلاقات، والمعاملات المالية. في معظم الأحيان، لا يدرك المستخدمون الحجم الحقيقي لما يُجمع عنهم."),
      para("المثال: تطبيق رياضي مجاني يبيع بيانات مسارات جري المستخدمين لشركات تأمين."),
      emptyLine(),

      sectionLabel("2. غياب الموافقة المستنيرة"),
      para("يوافق معظم المستخدمين على شروط الاستخدام دون قراءتها. كثير من جمع البيانات السلوكية يحدث ضمنياً عبر التطبيقات وبرامج التتبع الخفية."),
      para("السؤال الأخلاقي: هل يمكن اعتبار الموافقة حقيقية حين تكون آليات استخدام البيانات بهذا التعقيد؟"),
      emptyLine(),

      sectionLabel("3. التلاعب بدلاً من الإقناع"),
      para("يُشوّش الحث السلوكي الحدَّ الفاصل بين التوجيه المفيد والتلاعب النفسي. حين تستغل الخوارزميات التحيزات المعرفية (نفور الخسارة، الضغط الاجتماعي)، هل يتخذ المستخدم قراراً حراً فعلاً؟"),
      para("المثال: الأنماط المظلمة (Dark Patterns) في مواقع التجارة الإلكترونية التي تُصعّب إلغاء الاشتراك."),
      emptyLine(),

      sectionLabel("4. التحيز الخوارزمي والتمييز"),
      para("الأنظمة المدرَّبة على بيانات متحيزة تُكرّر الفوارق الاجتماعية وتُضاعفها. قد تُميّز درجات الائتمان السلوكي ضد الأقليات أو سكان المناطق الفقيرة."),
      para("المثال: نظام COMPAS لتقييم خطر إعادة الإجرام في القضاء الأمريكي ثبت تحيزه ضد الأمريكيين من أصول أفريقية."),
      emptyLine(),

      sectionLabel("5. أمان البيانات وسوء الاستخدام"),
      para("قواعد البيانات السلوكية أهداف عالية القيمة للقراصنة. حتى حين تُجمع لأغراض مشروعة، قد تُعاد استخدامها لأغراض أخرى: البيع لأطراف ثالثة، أو استخدامها في المراقبة الحكومية."),
      para("المثال: تسريب بيانات Cambridge Analytica التي استُخدمت للتأثير على توجهات الناخبين."),
      emptyLine(),

      sectionLabel("6. عدم التوازن في القوة"),
      para("تتراكم لدى الشركات الكبرى والحكومات ذكاء سلوكي هائل لا يملكه الأفراد. هذا يُفرز اختلالاً جوهرياً: المؤسسات تعرف عن المواطنين أكثر بكثير مما يعرف المواطنون عنها."),
      para("الحل: أطر تنظيمية مثل اللائحة الأوروبية لحماية البيانات (GDPR) وقانون الذكاء الاصطناعي الأوروبي (AI Act)."),
      emptyLine(),

      // ============ Shopping Recommendations ============
      heading1("سابعاً: أمثلة توصيات التسوق"),
      para("تُمثّل توصيات التسوق أبرز تطبيقات IoB التجارية. فيما يلي أمثلة تفصيلية:"),
      emptyLine(),

      heading2("أمازون — نظام التوصية الأكثر تطوراً"),
      bullet("'العملاء الذين اشتروا هذا المنتج اشتروا أيضاً...' — تصفية تعاونية على ملايين الملفات السلوكية."),
      bullet("يتتبع النظام: الوقت الذي قضيتَه في تصفح المنتج، وتاريخ الشراء، وقوائم الأمنيات، والسلة المتروكة."),
      bullet("يُولّد نظام التوصية 35% من إيرادات أمازون السنوية."),

      heading2("نتفليكس — التوصية القائمة على السلوك الكامل"),
      bullet("يُحلّل النظام: معدلات الإيقاف، وإعادة المشاهدة، والوقت المفضل للمشاهدة، وترتيب البحث."),
      bullet("ميزة 'لأنك شاهدت X' — توصية بالمحتوى المشابه بناءً على الأنماط السلوكية الكاملة."),
      bullet("التشغيل التلقائي (Autoplay) ذاته حث سلوكي يستغل القصور الذاتي لزيادة وقت المشاهدة."),

      heading2("سبوتيفاي — التوصية الموسيقية الذكية"),
      bullet("Discover Weekly: قائمة تشغيل أسبوعية مخصصة بالكامل بناءً على معدلات التخطي، والإعادة، والإضافة للمفضلة."),
      bullet("يُميّز النظام بين 'الموسيقى التي نستمع إليها في الصباح' و'ليلاً' بناءً على السلوك الفعلي."),

      heading2("نون وسوق — السياق الإقليمي"),
      bullet("تخصيص الصفحة الرئيسية وترتيب العروض بناءً على سجل التصفح والشراء لكل مستخدم."),
      bullet("إرسال إشعارات مخصصة بالعروض الموسمية لمن أبدوا اهتماماً بفئة منتج معينة."),
      emptyLine(),

      heading2("الآلية التقنية المشتركة لجميع أنظمة التوصية"),
      bullet("Collaborative Filtering: 'المستخدمون المشابهون لك اشتروا...'"),
      bullet("Content-Based Filtering: 'هذا المنتج يشبه ما اشتريتَه من قبل...'"),
      bullet("Deep Learning: تحليل الإشارات السلوكية الدقيقة (مدة التحديق، سرعة التمرير)."),
      bullet("Real-time Processing: تحديث التوصيات فورياً مع كل نقرة."),
      emptyLine(),

      // ============ Summary ============
      heading1("خلاصة"),
      para("إنترنت السلوك (IoB) يُمثّل تحولاً جذرياً في كيفية تفاعل التكنولوجيا مع الإنسان. فبينما ركّزت التقنيات السابقة على أتمتة المهام، يستهدف IoB فهم الإنسان وإعادة توجيه سلوكه."),
      emptyLine(),
      para("فرص IoB: تحسين الرعاية الصحية، ترشيد الاستهلاك، تعزيز الأمان، تخصيص التعليم، وزيادة كفاءة الخدمات."),
      emptyLine(),
      para("مخاطره: المراقبة الشاملة، التلاعب النفسي، التمييز الخوارزمي، وتركّز السلطة المعلوماتية."),
      emptyLine(),
      para("المستقبل: يستوجب IoB حوكمة راشدة تضمن استخدامه لمصلحة الأفراد لا للسيطرة عليهم — وذلك عبر تشريعات واضحة، وشفافية في الخوارزميات، واحترام حقيقي لإرادة الإنسان الحرة.", { bold: true }),
      emptyLine(), emptyLine(),
    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('IOB_Research.docx', buf);
  console.log('Done!');
});